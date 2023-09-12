---
title: 装饰者模式
tags: [design, decorator]
categories: 设计模式
---

> 装饰者模式：动态地将责任附加到对象上。若要扩展功能，装饰者提供了比继承更有弹性的替代方案。

<!-- more -->

## 装饰者模式的角色

- 抽象组件（Component）：定义一个对象接口，可以给这些对象动态地添加职责。
- 具体组件（ConcreteComponent）：是被封装对象的原始状态，定义了基本行为，但是装饰类可以改变它。
- 抽象装饰者（Decorator）：维持一个指向 Component 对象的指针，并定义一个与 Component 接口一致的接口。
- 具体装饰者（ConcreteDecorator）：定义了可动态添加到组件的额外行为。具体装饰类会重写装饰基类的方法，并在调用基类方法之前或之后加上自己的行为。

```puml
@startuml
interface Component {
    + operation()
}
class ConcreteComponent {
    + operation()
}
class Decorator {
    - component: Component
    + operation()
}
class ConcreteDecoratorA {
    + operation()
    + extraOperation()
}
class ConcreteDecoratorB {
    + operation()
    + extraOperation()
    + anotherOperation()
}
Component <|-- ConcreteComponent
Component <|-- Decorator
Decorator <|-- ConcreteDecoratorA
Decorator <|-- ConcreteDecoratorB
@enduml
```

## 装饰者模式的应用场景

- 扩展类功能：装饰者模式允许你通过创建装饰器类来扩展现有类的功能，而不必修改原始类的代码。这对于已经存在的、不容易修改的类非常有用，或者在不希望修改类的源代码的情况下扩展其功能。

- 动态添加功能：你可以根据需要动态地添加不同的装饰器，以增加对象的功能。这种方式使得可以在运行时选择不同的装饰器组合，而不是在编译时确定。

- 避免类爆炸：当有多种组合方式需要考虑时，使用继承可能会导致类的爆炸性增长。装饰者模式允许你将不同的功能分解为独立的装饰器，以避免创建大量子类。

- 开放封闭原则：装饰者模式符合开放封闭原则，即对扩展开放，对修改封闭。这意味着你可以轻松地添加新的装饰器类，而不必修改现有的代码。

- 不破坏对象结构：装饰者模式不会破坏原始对象的结构，因为它通过组合而不是继承来添加新功能。

- 动态组合：你可以动态地组合多个装饰器，以实现各种不同的组合效果。这使得你可以根据需要构建复杂的对象。

### IO

IO 类就是装饰者模式的一个典型应用，如 `BufferedInputStream`、`BufferedOutputStream`、`DataInputStream`、`DataOutputStream` 等。

```puml
@startuml
interface InputStream {
    + read()
}
class FileInputStream {
    + read()
}
class FilterInputStream {
    - in: InputStream
    + read()
}
class ByteArrayInputStream {
    - in: InputStream
    + read()
}
class DataInputStream {
    - in: InputStream
    + read()
}
class DigestInputStream {
    - in: InputStream
    + read()
}
class BufferedInputStream {
    - in: InputStream
    + read()
}
class GZIPInputStream {
    - in: InputStream
    + read()
}
class InflaterInputStream {
    - in: InputStream
    + read()
}
InputStream <|-- FileInputStream
InputStream <|-- FilterInputStream
InputStream <|-- ByteArrayInputStream
FilterInputStream <|-- BufferedInputStream
FilterInputStream <|-- DataInputStream
FilterInputStream <|-- DigestInputStream
FilterInputStream <|-- GZIPInputStream
FilterInputStream <|-- InflaterInputStream
@enduml
```

例如，GzipInputStream 类就是一个装饰者，它继承自 FilterInputStream 类，而 FilterInputStream 类又继承自 InputStream 类。GzipInputStream 类在读取数据之前，会先将数据解压缩，然后再读取。

```java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.zip.GZIPInputStream;

public class GzipUtils {
    public static byte[] decompress(byte[] compressedData) throws IOException {
        try (
            ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(compressedData);
            GZIPInputStream gzipInputStream = new GZIPInputStream(byteArrayInputStream);
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()
        ) {
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = gzipInputStream.read(buffer)) != -1) {
                byteArrayOutputStream.write(buffer, 0, bytesRead);
            }
            return byteArrayOutputStream.toByteArray();
        }
    }
}

```

- `DataInputStream`：

作用：DataInputStream 用于从输入流中读取原始数据类型的数据，如整数、浮点数、字符等。它提供了方法来方便地读取这些数据类型，而无需手动进行字节转换。
典型用途：用于读取二进制文件或与其他系统通信时，处理基本数据类型的输入。

- `BufferedInputStream`：

作用：BufferedInputStream 用于缓冲输入流，从而提高读取数据的效率。它通过在内存中维护一个缓冲区来减少实际的物理读取操作，从而减少了 I/O 操作的次数。
典型用途：在读取大文件或者需要频繁读取的数据时，可以使用 BufferedInputStream 来减少磁盘或网络 I/O 的负担，提高性能。

- `DigestInputStream`：

作用：DigestInputStream 是一个装饰器（Decorator）类，它可以包装其他输入流，并计算输入流中数据的哈希值（如 MD5、SHA-1 等）。它提供了一种在读取数据的同时计算数据完整性校验值的方式。
典型用途：用于验证下载文件的完整性或者进行数据校验的场景，以确保数据没有被篡改。

```java
public class FileUtils {
    /**
     * 写一个获取文件MD5值的方法
     */
    public static String getFileMD5Str(String filePath) {
        try {
            // 创建一个 FileInputStream 来读取文件内容
            FileInputStream fileInputStream = new FileInputStream(filePath);

            // 创建一个 MessageDigest 实例，用于计算哈希值
            MessageDigest md = MessageDigest.getInstance("MD5");

            // 创建 DigestInputStream，它会包装 FileInputStream 并在读取数据时计算哈希值
            DigestInputStream digestInputStream = new DigestInputStream(fileInputStream, md);

            // 获取计算得到的哈希值
            byte[] hashBytes = md.digest();

            // 将哈希值转换为十六进制字符串
            StringBuilder hashStringBuilder = new StringBuilder();
            for (byte b : hashBytes) {
                hashStringBuilder.append(String.format("%02x", b));
            }
            // 关闭输入流
            digestInputStream.close();

            return hashStringBuilder.toString();

        } catch (IOException | NoSuchAlgorithmException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }
}
```

- `GZIPInputStream`：

作用：GZIPInputStream 用于解压缩经过 GZIP 压缩的数据流。它能够将压缩后的数据解压成原始的数据。
典型用途：在接收到经过 GZIP 压缩的数据流（如 HTTP 响应或文件）时，可以使用 GZIPInputStream 来解压数据。

- `InflaterInputStream`：

作用：InflaterInputStream 用于解压缩数据，通常用于解压缩经过 Deflate 压缩的数据流。
典型用途：在需要处理 Deflate 压缩的数据流时，可以使用 InflaterInputStream 解压数据，例如在处理 ZIP 文件或 HTTP 响应中的数据时。

### 咖啡

```puml
@startuml

interface Coffee {
    +getDescription(): String
    +cost(): double
}

class Espresso {
    +getDescription(): String
    +cost(): double
}

class HouseBlend {
    +getDescription(): String
    +cost(): double
}

abstract class CoffeeDecorator {
    -decoratedCoffee: Coffee
    +CoffeeDecorator(decoratedCoffee: Coffee)
    +getDescription(): String
    +cost(): double
}

class MilkDecorator {
    +MilkDecorator(decoratedCoffee: Coffee)
    +getDescription(): String
    +cost(): double
}

class SugarDecorator {
    +SugarDecorator(decoratedCoffee: Coffee)
    +getDescription(): String
    +cost(): double
}

Coffee <|-- Espresso
Coffee <|-- HouseBlend
Coffee <|-- CoffeeDecorator
CoffeeDecorator <|-- MilkDecorator
CoffeeDecorator <|-- SugarDecorator
@enduml
```

```java
public interface Coffee {
    String getDescription();
    double cost();
}

public class Espresso implements Coffee {
    @Override
    public String getDescription() {
        return "Espresso";
    }

    @Override
    public double cost() {
        return 1.99;
    }
}

public class HouseBlend implements Coffee {
    @Override
    public String getDescription() {
        return "House Blend Coffee";
    }

    @Override
    public double cost() {
        return 0.89;
    }
}

public abstract class CoffeeDecorator implements Coffee {
    protected final Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee decoratedCoffee) {
        this.decoratedCoffee = decoratedCoffee;
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }

    @Override
    public double cost() {
        return decoratedCoffee.cost();
    }
}

public class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee decoratedCoffee) {
        super(decoratedCoffee);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Milk";
    }

    @Override
    public double cost() {
        return super.cost() + 0.5;
    }
}

public class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee decoratedCoffee) {
        super(decoratedCoffee);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Sugar";
    }

    @Override
    public double cost() {
        return super.cost() + 0.2;
    }
}
```

```java
public class CoffeeShop {
    public static void main(String[] args) {
        // 创建一杯浓缩咖啡
        Coffee espresso = new Espresso();
        System.out.println(espresso.getDescription() + " $" + espresso.cost());

        // 创建一杯浓缩咖啡并加牛奶和糖
        Coffee espressoWithMilkAndSugar = new SugarDecorator(new MilkDecorator(new Espresso()));
        System.out.println("Description: " + espressoWithMilkAndSugar.getDescription());
        System.out.println("Cost: $" + espressoWithMilkAndSugar.cost());

         // 创建一杯混合咖啡并加糖
        Coffee houseBlendWithSugar = new SugarDecorator(new HouseBlend());
        System.out.println("Description: " + houseBlendWithSugar.getDescription());
        System.out.println("Cost: $" + houseBlendWithSugar.cost());
    }
}
```

### Executor

org.apache.ibatis.executor.Executor 里也使用到了装饰者模式

```puml
@startuml

interface Executor << interface >>

class BaseExecutor {
  + BaseExecutor(Configuration, Transaction): 
}
class BatchExecutor {
  + BatchExecutor(Configuration, Transaction): 
}
class CachingExecutor {
  + CachingExecutor(Executor): 
}
class ReuseExecutor {
  + ReuseExecutor(Configuration, Transaction): 
}
class SimpleExecutor {
  + SimpleExecutor(Configuration, Transaction): 
}

Executor     <--  BaseExecutor        
BaseExecutor    <--  BatchExecutor    
Executor  <--  CachingExecutor        
BaseExecutor    <--  ReuseExecutor    
BaseExecutor   <--  SimpleExecutor    
@enduml

```

其中 `CachingExecutor` 就是一种装饰者，对于Exceutor执行方法前后进行了缓存操作。

```java
    public int update(MappedStatement ms, Object parameterObject) throws SQLException {
    flushCacheIfRequired(ms); //缓存清除
    return delegate.update(ms, parameterObject);
    }

    public <E> List<E> query(MappedStatement ms, Object parameterObject, RowBounds rowBounds, ResultHandler resultHandler, CacheKey key, BoundSql boundSql)
      throws SQLException {
    Cache cache = ms.getCache();
    if (cache != null) {
      flushCacheIfRequired(ms);
      if (ms.isUseCache() && resultHandler == null) {
        ensureNoOutParams(ms, parameterObject, boundSql);
        @SuppressWarnings("unchecked")
        List<E> list = (List<E>) tcm.getObject(cache, key);
        if (list == null) {
          list = delegate.<E> query(ms, parameterObject, rowBounds, resultHandler, key, boundSql);
          tcm.putObject(cache, key, list); // 缓存添加
        }
        return list;
      }
    }
    return delegate.<E> query(ms, parameterObject, rowBounds, resultHandler, key, boundSql);
  }
```