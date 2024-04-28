# 并发

## 基础

### Thread

### Sychronized

### Volatile

### CAS（Compare And Swap）

```java

private static final Unsafe unsafe = Unsafe.getUnsafe();

private static final long valueOffset;

static {
    try {
        valueOffset = unsafe.objectFieldOffset
            (AtomicInteger.class.getDeclaredField("value"));
    } catch (Exception ex) { throw new Error(ex); }
}

private volatile int value;

public final int getAndAddInt(Object var1, long var2, int var4) {
    int var5;
    do {
        var5 = this.getIntVolatile(var1, var2);
    } while(!this.compareAndSwapInt(var1, var2, var5, var5 + var4));

    return var5;
}
```

#### 自旋无限循环性能问题

- 自旋等待的线程会一直占用 CPU，导致 CPU 利用率过高，采用分段CAS优化

`LongAdder`

分段CAS优化当某一个线程如果对一个值更新是，可以看对这个值进行分段更新，每一段叫做一个Cell，在更新每一个Cell的时候，发现说出现了很难更新它的值，出现了多次 CAS失败了，自旋的时候，进行自动迁移段，它会去尝试更新别的分段Cell的值，这样的话就可以让一个线程不会盲目的CAS自旋等待一个更新分段cell的值。

#### ABA问题

如果某个值一开始是A，后来变成了B，然后又变成了A，你本来期望的是值如果是第一个A才会设置新值，结果第二个A一比较也ok，也设置了新值，跟期望是不符合的。

解决方案：加版本号，每次更新的时候，版本号加1，这样的话，即使值一样，版本号不一样，也不会出现ABA问题。

```java
public boolean compareAndSet(V  expectedReference,
                V  newReference,
                int expectedStamp,
                int newStamp) {

Pair<V> current = pair;
return
    // 比对引用
    expectedReference == current.reference &&
    // 比对版本号
    expectedStamp == current.stamp &&
    ((newReference == current.reference &&
    newStamp == current.stamp) ||
    casPair(current, Pair.of(newReference, newStamp)));
}

private boolean casPair(Pair<V> cmp, Pair<V> val) {
    return UNSAFE.compareAndSwapObject(this, pairOffset, cmp, val);
}
```

### AQS (AbstractQueuedSynchronizer)

## 组件

### ReentrantLock = Volatile + AQS + CAS

### Atomic = Volatile + CAS

### CountDownLatch = Volatile + AQS

### Smeaphore = Volatile + AQS

## 集合

### ConcurrentHashMap = Volatile + CAS + Sychronized

### ConcurrentLinkedQueue = Volatile + CAS

### CopyOnWriteArrayList = Volatile + ReentrantLock

### ArrayBlockingQueue = Condition + ReentrantLock

### LinkedBlockingQueue = Autmic + Condition + ReentrantLock