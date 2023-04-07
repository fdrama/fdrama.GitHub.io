---
title: 单例模式
tags: [design, singleton]
categories: 设计模式
---

> Java单例模式是常见设计模式之一，从定义上看，它似乎是一种简单的设计模式，但当涉及到实现时，它会带来很多问题。在本文中，我们将了解单例设计模式的原则，探索实现单例设计模式的不同方法，以及使用它的一些最佳实践。

## 单例模式原则

- 私有构造方法，限制其他类实例化该类。
- 私有静态示例变量，该类的唯一实例。
- 公共静态方法，返回该类的唯一实例。

## 单例模式实现

### 饿汉

在类加载的时候创建实例。快速初始化的缺点是，即使应用程序可能没有使用该方法，也会创建该实例。

如果您的单例类没有使用大量资源，则可以使用这种方法。

```java
public class EagerInitializedSingleton {

    private static final EagerInitializedSingleton instance = new EagerInitializedSingleton();

    
    private EagerInitializedSingleton(){}

    public static EagerInitializedSingleton getInstance() {
        return instance;
    }
}

```

### 静态代码块

静态代码块和上面的饿汉基本一致，就是可以进行异常处理，当然缺点也一样。

```java
public class StaticBlockSingleton {

    private static StaticBlockSingleton instance;

    private StaticBlockSingleton(){}

    // static block initialization for exception handling
    static {
        try {
            instance = new StaticBlockSingleton();
        } catch (Exception e) {
            throw new RuntimeException("Exception occurred in creating singleton instance");
        }
    }

    public static StaticBlockSingleton getInstance() {
        return instance;
    }
}
```

### 懒汉

在调用方法的时候才会创建实例。

```java
public class LazyInitializedSingleton {

    private static LazyInitializedSingleton instance;

    private LazyInitializedSingleton(){}

    public static LazyInitializedSingleton getInstance() {
        if (instance == null) {
            instance = new LazyInitializedSingleton();
        }
        return instance;
    }
}
```

在多线程环境下，如果多个线程同时在if条件中，调用会存在线程安全问题，会破坏单例模式。

### 线程安全

```java
public class ThreadSafeSingleton {

    private static ThreadSafeSingleton instance;

    private ThreadSafeSingleton(){}

    public static synchronized ThreadSafeSingleton getInstance() {
        if (instance == null) {
            instance = new ThreadSafeSingleton();
        }
        return instance;
    }

    // double-checked
    public static ThreadSafeSingleton getInstanceUsingDoubleLocking() {
    if (instance == null) {
        synchronized (ThreadSafeSingleton.class) {
            if (instance == null) {
                instance = new ThreadSafeSingleton();
            }
        }
    }
    return instance;
}

}
```

### 静态内部类

注意包含单例类实例的私有内部静态类。当加载单例类时，SingletonHelper类不会加载到内存中，只有当有人调用getInstance()方法时，该类才会加载并创建单例类实例。这是单例类使用最广泛的方法，因为它不需要同步。

```java
public class BillPughSingleton {

    private BillPughSingleton(){}

    private static class SingletonHelper {
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }

    public static BillPughSingleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}
```

反射可以破坏上面的所有单例实现。

```java
import java.lang.reflect.Constructor;

public class ReflectionSingletonTest {

    public static void main(String[] args) {
        EagerInitializedSingleton instanceOne = EagerInitializedSingleton.getInstance();
        EagerInitializedSingleton instanceTwo = null;
        try {
            Constructor[] constructors = EagerInitializedSingleton.class.getDeclaredConstructors();
            for (Constructor constructor : constructors) {
                // This code will destroy the singleton pattern
                constructor.setAccessible(true);
                instanceTwo = (EagerInitializedSingleton) constructor.newInstance();
                break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(instanceOne.hashCode());
        System.out.println(instanceTwo.hashCode());
        // not equal
        System.out.println(instanceOne.equals(instanceTwo));


    }

}
```

### 枚举

因为Java确保任何enum值在Java程序中只实例化一次。因为Java Enum值是全局可访问的，所以单例也是如此。

```java
public enum EnumSingleton {

    INSTANCE;

    public static void doSomething() {
        // do something
    }
}
```

### 序列化和单例

```java
import java.io.Serializable;

public class SerializedSingleton implements Serializable {

    private static final long serialVersionUID = -7604766932017737115L;

    private SerializedSingleton(){}

    private static class SingletonHelper {
        private static final SerializedSingleton instance = new SerializedSingleton();
    }

    public static SerializedSingleton getInstance() {
        return SingletonHelper.instance;
    }

}
```

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;

public class SingletonSerializedTest {

    public static void main(String[] args) throws FileNotFoundException, IOException, ClassNotFoundException {
        SerializedSingleton instanceOne = SerializedSingleton.getInstance();
        ObjectOutput out = new ObjectOutputStream(new FileOutputStream(
                "filename.ser"));
        out.writeObject(instanceOne);
        out.close();

        // deserialize from file to object
        ObjectInput in = new ObjectInputStream(new FileInputStream(
                "filename.ser"));
        SerializedSingleton instanceTwo = (SerializedSingleton) in.readObject();
        in.close();

        // not equal
        System.out.println("instanceOne hashCode="+instanceOne.hashCode());
        System.out.println("instanceTwo hashCode="+instanceTwo.hashCode());
    }
}
```

序列化破坏了单例模式，但是可以通过readResolve()解决。

```java
protected Object readResolve() {
    return getInstance();
}
```

```out
instanceOne hashCode=1359484306
instanceTwo hashCode=1359484306
```