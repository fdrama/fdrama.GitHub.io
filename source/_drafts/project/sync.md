# 并发

- 可见性，一句话讲就是多个线程中有读有写操作同一个变量的时候，线程间可以互相知道，可见的意思。
- 有序性，一句话讲就是由于代码执行顺序可能被重排序，volatile可以保证代码行数按顺序执行。
- 原子性，一句话讲就是当多个线程进行同时写同一个变量的时候，只能有一个线程进这一操作。

## 基础

### Thread

### Sychronized

#### 实现原理

#### 锁升级机制

- 无锁态

表示第一次对刚创建的对象或者类加锁时的状态。我发现只有一个线程在操作代码块的资源，压根不需要加锁。此时会处于无锁态。

- 偏向锁

类似于贴标签，表示这个资源暂时属于某个线程

- 轻量级锁

轻量锁，底层是CAS自旋的操作，所以也叫自旋锁

- 重量级锁

重量级锁，底层是操作系统的mutex互斥锁，底层是操作系统的内核态的锁，用户态是不能直接操作内核态中资源的，只能通知内核态来操作

JVM的进程只是处于用户态的进程，所以需要向操作系统申请，这个过程肯定会很消耗资源的。

比如，synchronized的本质是JVM用户空间的一个进程（处于用户态）向操作系统(内核态)发起一个lock的锁指令操作 。

monitorenter、monitorexit。

![alt text](image-6.png)

### Sleep, Wait, Notify

### Volatile

使用场景：

1、 多个线程对同一个变量有读有写的时候

2、 多个线程需要保证有序性和可见性的时候

简单的讲，一句话：就是刷新主内存，强制过期其他线程的工作内存。

JVM内存模型

堆（Heap）：线程共享。所有的对象实例以及数组都要在堆上分配。回收器主要管理的对象。
方法区（Method Area）：线程共享。存储类信息、常量、静态变量、即时编译器编译后的代码。
方法栈（JVM Stack）：线程私有。存储局部变量表、操作栈、动态链接、方法出口，对象指针。
本地方法栈（Native Method Stack）：线程私有。为虚拟机使用到的Native 方法服务。如Java使用c或者c++编写的接口服务时，代码在此区运行。
程序计数器（Program Counter Register）：线程私有。有些文章也翻译成PC寄存器（PC Register），同一个东西。它可以看作是当前线程所执行的字节码的行号指示器。指向下一条要执行的指令。

![alt text](image-4.png)

JVM 逻辑内存模型

![alt text](image-3.png)

![alt text](image-5.png)

JMM的指令和使用规则

volatile保证可见性的原理，还是之前总结的一句话：写入主内存数据时，刷新主内存值之后，强制过期其他线程的工作内存，底层是因为lock、unlock操作的原则导致的，其他线程读取变量的时候必须重新加载主内存的最新数据，从而保证了可见性。

有序性 happen-before 规则

防止指令重排

volatile变量规则：对一个变量的写操作先行发生于后面对这个变量的读操作。volatile变量写，再是读，必须保证是先写，再读。

高速缓存、RAM内存、L3，CPU内部线程私有的内存L1、L2缓存，通过总线从逐层将缓存读入每一级缓存。如下流程所示：

RAM内存->高速缓存（L4一般位于总线）->L3级缓存（CPU共享）->L2级缓存（CPU内部私有）->L1级缓存（CPU内部私有）。

这样当java中多个线程执行的时候，实际是交给CPU的每个寄存器执行每一个线程。一套寄存器+程序计数器可以执行一个线程，平常我们说的4核8线程，实际指的是8个寄存器。所以Java多线程执行的逻辑对应CPU组件如下图所示：

### CAS（Compare And Swap）

- value
- valueOffset
- unsafe

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

- state
- owner
- AQS(等待队列 queue)

![alt text](image.png)

```java
static final class NonfairSync extends Sync {
    private static final long serialVersionUID = 7316153563782823691L;

    /**
     * Performs lock.  Try immediate barge, backing up to normal
     * acquire on failure.
     */
    final void lock() {
        // 首先进行的操作就是一个CAS，更新了volatile变量state，由0变为1
        if (compareAndSetState(0, 1))
            // 设置当前线程为独占线程 owner
            setExclusiveOwnerThread(Thread.currentThread());
        else
            acquire(1);
    }

    protected final boolean tryAcquire(int acquires) {
        return nonfairTryAcquire(acquires);
    }
}

protected final boolean compareAndSetState(int expect, int update) {
    // See below for intrinsics setup to support this
    return unsafe.compareAndSwapInt(this, stateOffset, expect, update);
}
```

- 无冲突加锁步骤

![alt text](image-1.png)

- 有冲突场景

```java
public final void acquire(int arg) {
    // 再次尝试获取锁
    if (!tryAcquire(arg) &&
        // 如果获取锁失败，将当前线程加入等待队列
        // 入队后会再次尝试获取锁，失败就会将线程挂起 park
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))
        selfInterrupt();
}

protected final boolean tryAcquire(int acquires) {
    return nonfairTryAcquire(acquires);
}

final boolean nonfairTryAcquire(int acquires) {
    final Thread current = Thread.currentThread();
    int c = getState();
    if (c == 0) {
        if (compareAndSetState(0, acquires)) {
            setExclusiveOwnerThread(current);
            return true;
        }
    }
    // 可重入
    else if (current == getExclusiveOwnerThread()) {
        int nextc = c + acquires;
        if (nextc < 0) // overflow
            throw new Error("Maximum lock count exceeded");
        setState(nextc);
        return true;
    }
    return false;
}

private Node addWaiter(Node mode) {
    Node node = new Node(Thread.currentThread(), mode);
    // Try the fast path of enq; backup to full enq on failure
    Node pred = tail;
    if (pred != null) {
        node.prev = pred;
        // 双向链表
        if (compareAndSetTail(pred, node)) {
            pred.next = node;
            return node;
        }
    }
    enq(node);
    return node;
}

// 将当前线程加入等待队列 双向链表
private Node enq(final Node node) {
    for (;;) {
        Node t = tail;
        // 第一次循环，初始化一个新的节点
        if (t == null) { // Must initialize
            // 通过CAS更新头节点 tail和head指向了空的new Node()。
            if (compareAndSetHead(new Node()))
                tail = head;
        } else {
            // 入参node节点的prev指向了t所指向的空Node。
            node.prev = t;
            // 通过CAS更新尾节点，将tail指向到入参node节点。
            if (compareAndSetTail(t, node)) {
                t.next = node;
                return t;
            }
        }
    }
}
```

![alt text](image-2.png)

#### 释放锁 unlock

```java
public void unlock() {
    sync.release(1);
}

public final boolean release(int arg) {
  if (tryRelease(arg)) {
    Node h = head;
    if (h != null && h.waitStatus != 0)
      unparkSuccessor(h);
    return true;
  }
  return false;
}
```

核心分为了2步：

1） tryRelease方法，释放state和owner变量

2） unparkSuccessor方法，唤醒队列元素

分别来看一下，首先释放变量tryRelease方法：

```java
 protected final boolean tryRelease(int releases) {
  // 加锁数量 
  int c = getState() - releases;
  if (Thread.currentThread() != getExclusiveOwnerThread())
    throw new IllegalMonitorStateException();
  boolean free = false;
  // 释放锁
  if (c == 0) {
    free = true;
    setExclusiveOwnerThread(null);
  }
  // 更新state
  setState(c);
  return free;
}
```

释放成功锁后，使用了h指针指向了当前队列的头部，判断一下队列中是否有等待的元素，注意对头元素waitStatus不能是0，如果是0，说明队列只有一个空节点，队列中没有等待元素。因为入队元素后会将头结点的waitStatus改成-1，SIGNAL。

```java
private void unparkSuccessor(Node node) {
  int ws = node.waitStatus;
  if (ws < 0)
    // 首先把head节点waitStatus从-1改为0。
    compareAndSetWaitStatus(node, ws, 0);
  // 找到下一个节点
  Node s = node.next;
  if (s == null || s.waitStatus > 0) {
    s = null;
    for (Node t = tail; t != null && t != node; t = t.prev)
      if (t.waitStatus <= 0)
        s = t;
  }

  if (s != null)
    // 唤醒线程
    LockSupport.unpark(s.thread);
}
```

#### 公平锁，非公平锁

加锁的时候，一个if判断

- 非公平锁, 会直接尝试获取锁，如果获取失败，再将线程加入等待队列
- 公平锁，会先判断队列中是否有等待的线程，如果有，先将线程加入等待队列，再尝试获取锁

#### 重入锁，非重入锁

同一个线程可以使用同一个ReentrantLock进行反复加锁。 加锁，state会在现有值上加+1，每再次加一次锁

另外，释放锁的话，肯定需要释放所多次，同一个线程加锁了几次，就需要释放几次，需要将state值恢复为0才算真正的释放锁，别的线程才能获取到。

#### 独占锁，共享锁

独占锁，只能有一个线程获取锁，其他线程只能等待，直到锁被释放

默认reentrantLock.lock创建的锁是什么的呢？非公平的可重入独占锁！

#### 核心组件

## 组件

### ReentrantLock = Volatile + AQS + CAS

### Atomic = Volatile + CAS

### CountDownLatch = Volatile + AQS

### Smeaphore = Volatile + AQS

### ThreadLocal = ThreadLocalMap

## 集合

### ConcurrentHashMap = Volatile + CAS + Sychronized

### ConcurrentLinkedQueue = Volatile + CAS

### CopyOnWriteArrayList = Volatile + ReentrantLock

### ArrayBlockingQueue = Condition + ReentrantLock

### LinkedBlockingQueue = Autmic + Condition + ReentrantLock