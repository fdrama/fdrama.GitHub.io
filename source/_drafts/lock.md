# 简单的互斥锁

```java
public class SimpleLock {

    private static Logger logger = LoggerFactory.getLogger(SimpleLock.class);

    private final AtomicBoolean lock = new AtomicBoolean(false);

    public SimpleLock(){

    }

    /**
     * 尝试抢锁（默认尝试1分钟）
     * @return
     */
    public boolean tryLock(){
        return tryLock(60,TimeUnit.SECONDS);
    }

    /**
     * 尝试加锁（等待指定时间，如超时则返回false）
     * @param wait
     * @param unit
     * @return
     * @throws InterruptedException
     */
    public boolean tryLock(int wait, TimeUnit unit){
        if (unit == null){
            unit = TimeUnit.SECONDS;
        }
        long waitMillis = unit.convert(wait,TimeUnit.MILLISECONDS);
        if (waitMillis < 0) waitMillis = 0;
        long stopTime = SystemClock.now() + waitMillis;

        boolean locked = false;
        synchronized (lock){
            try {
                do {
                    if ((locked == lock.compareAndSet(false, true))) {
                        break;
                    } else {
                        long wTime = stopTime - SystemClock.now();

                        if (wTime <= 0) break;
                        lock.wait(wTime);
                    }
                } while (SystemClock.now() <= stopTime);
            }catch (Exception e){
                System.out.println("SimpleLock尝试加锁时出错:"+e.getMessage());
                logger.error("SimpleLock尝试加锁时出错：{}",e.getMessage());
            }
        }
        return locked;
    }

    /**
     * 释放锁（注：已获得锁时才能调用）
     */
    public void unlock(){
        try {
            synchronized (lock) {
                lock.set(false);
                lock.notifyAll();
            }
        }catch (Exception e){
            logger.error("SimpleLock释放锁时出错：{}",e.getMessage());
        }
    }

    /**
     * 在锁内执行
     * @param wait
     * @param unit
     * @param callback
     */
    public <T> T inLock(int wait, TimeUnit unit, Callback<T> callback){
        if (callback == null){
            return null;
        }
        boolean locked = false;
        try{
            if (locked = tryLock(wait,unit)){
                return callback.onGetLock();
            }
            return callback.onTimeout();
        }finally {
            if (locked){
                unlock();
            }
            callback.onCompleted();
        }
    }


    public interface Callback<T>{

        T onGetLock();

        T onTimeout();

        void onCompleted();
    }

}


public class TaskLockHolder {

    private static ConcurrentHashMap<Long, SimpleLock> locks = new ConcurrentHashMap<>();

    /**
     * 获取锁
     * @return
     */
    public synchronized static SimpleLock getLock(long taskId,SimpleLock defaultLock) {
        if (defaultLock == null){
            defaultLock = new SimpleLock();
        }
        SimpleLock lock = locks.get(taskId);
        if (null == lock){
            locks.put(taskId,defaultLock);
            lock = defaultLock;
        }
        return lock;
    }

    /**
     * 注销锁
     * @param key
     */
    public static void release(long key) {
        locks.remove(key);
    }

}

```

## 使用方法

```java
SimpleLock lock = TaskLockHolder.getLock(taskId,new SimpleLock());
lock.inLock(50, TimeUnit.MILLISECONDS, new SimpleLock.Callback<Void>() {
    @Override
    public Void onGetLock() {
        // do something
        return null;
    }
    @Override
    public Void onTimeout() {
        // do something
        throw new RuntimeException("抢锁超时");
    }
    @Override
    public void onCompleted() {
        // do something
    }
});
```
