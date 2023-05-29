---
title: HashMap
tags: [source code, java]
categories: 源码解读
---

## 数据结构

**数组+链表**，HashMap类中有一个非常重要的字段，就是 `Node<K,V>[] table`，即哈希桶数组，它是一个Node的数组，Node是HashMap的一个内部类，实现了Map.Entry接口，本质是就是一个映射(键值对)。

```java
transient Node<K,V>[] table;


static class Node<K,V> implements Map.Entry<K,V> {
    final int hash;
    final K key;
    V value;
    Node<K,V> next;

    Node(int hash, K key, V value, Node<K,V> next) {
        this.hash = hash;
        this.key = key;
        this.value = value;
        this.next = next;
    }

    public final K getKey()        { return key; }
    public final V getValue()      { return value; }
    public final String toString() { return key + "=" + value; }

    public final int hashCode() {
        return Objects.hashCode(key) ^ Objects.hashCode(value);
    }

    public final V setValue(V newValue) {
        V oldValue = value;
        value = newValue;
        return oldValue;
    }

    public final boolean equals(Object o) {
        if (o == this)
            return true;
        if (o instanceof Map.Entry) {
            Map.Entry<?,?> e = (Map.Entry<?,?>)o;
            if (Objects.equals(key, e.getKey()) &&
                Objects.equals(value, e.getValue()))
                return true;
        }
        return false;
    }
}
```

## 初始化

当我们 `new HashMap<>()`的时候发生了什么，我看看HashMap的构造方法，就是对以下的几个属性进行了初始化设置。值得一提的是，`Node<K,V>[] table`的初始化是在添加第一个元素的时候，执行`resize()`方法设置的，默认$16$。

```java
public HashMap() {
    // 设置负载因子
    this.loadFactor = DEFAULT_LOAD_FACTOR; // all other fields defaulted
}

/**
 * 指定容量
 */
public HashMap(int initialCapacity) {
    this(initialCapacity, DEFAULT_LOAD_FACTOR);
}

public HashMap(int initialCapacity, float loadFactor) {
    if (initialCapacity < 0)
        throw new IllegalArgumentException("Illegal initial capacity: " +
                                            initialCapacity);
    if (initialCapacity > MAXIMUM_CAPACITY)
        initialCapacity = MAXIMUM_CAPACITY;
    if (loadFactor <= 0 || Float.isNaN(loadFactor))
        throw new IllegalArgumentException("Illegal load factor: " +
                                            loadFactor);
    this.loadFactor = loadFactor;
    // 计算HashMap的容量大小，保证HashMap的容量大小始终为2的幂次方，这样可以通过位运算来快速计算键值对的索引位置，提高HashMap的性能。
    this.threshold = tableSizeFor(initialCapacity);
}

/**
 * HashMap中实际存在的键值对数量
 */
transient int size;
/**
 * modCount字段主要用来记录HashMap内部结构发生变化的次数，主要用于迭代的快速失败
 */
transient int modCount;
/**
 * threshold = length * Load factor
 * threshold就是在此Load factor和length(数组长度)对应下允许的最大元素数目，超过这个数目就重新resize(扩容)。
 */
int threshold;
/**
 * 负载因子，默认的负载因子0.75是对空间和时间效率的一个平衡选择
 */
final float loadFactor;

```

## put

我们从`put(K key, V value)`方法入手，看看HashMap的详细执行过程。

```java
public V put(K key, V value) {
    return putVal(hash(key), key, value, false, true);
}

final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    // 1 判断table是否为空，或者lenght==0， 添加第一个元素的时候就会走进这个方法
    if ((tab = table) == null || (n = tab.length) == 0)
        // 1.2 对table 进行扩容
        n = (tab = resize()).length;
    // 2. 根据键值key计算hash值 ((n -1) & hash) 得到插入的数组索引i，如果table[i]==null，直接新增节点，添加到数组中
    if ((p = tab[i = (n - 1) & hash]) == null)
        tab[i] = newNode(hash, key, value, null);
    else {
        Node<K,V> e; K k;
        // 3. 判断table[i]的首个元素p的hash值是否相同，直接覆盖value
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;
        // 4. 判断table[i] 是否为treeNode，即table[i] 是否是红黑树，如果是红黑树，则直接在树中插入键值对，否则转向5
        else if (p instanceof TreeNode)
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
        else {
            //5. 遍历table[i] 链表，binCount是一个计数器，用于记录链表中键值对的数量。
            for (int binCount = 0; ; ++binCount) {
                // 5.1 如果当前节点p的下一个节点e为null，说明当前节点是链表的最后一个节点，可以将新的键值对插入到链表的末尾。
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);
                    if (binCount >= TREEIFY_THRESHOLD - 1) // 默认8
                        treeifyBin(tab, hash); // 还需要满足 table.length >= 64 才转换为红黑树
                    break;
                }
                // 5.2 如果链表中已经存在一个键值对的哈希值和要插入的键值对的哈希值相同，并且键值对的key也相同，直接覆盖value 
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    break;
                // 5.3 如果链表中不存在相同的键值对，就将当前节点p指向下一个节点e，继续遍历链表。
                p = e;
            }
        }
        // 值覆盖
        if (e != null) { // existing mapping for key
            V oldValue = e.value;
            // onlyIfAbsent || value == null 不覆盖值
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    // 6. 操作次数++
    ++modCount;
    // 7. 插入成功后，超过最大容量 就扩容。
    if (++size > threshold)
        resize();
    afterNodeInsertion(evict);
    return null;
}
```

下面我们针对上面的代码展开讲解，设计哈希函数，扩容机制，红黑树

### 哈希函数

不管增加、删除、查找键值对，都需要定位到哈希桶数组的位置，HashMap的数据结构是数组和链表的结合，我们希望这个HashMap里面的元素位置尽量分布均匀些，尽量使得每个位置上的元素数量只有一个，那么当我们用hash算法求得这个位置的时候，马上就可以知道对应位置的元素就是我们要的，不用遍历链表，大大优化了查询的效率。HashMap定位数组索引位置，直接决定了hash方法的离散性能。先看看源码的实现；

```java
// Hash算法本质上就是三步：取key的hashCode值、高位运算、取模运算。
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
// 计算该对象在table数组的索引。 取模运算
i = (n - 1) & hash
```

这里有两个知识点，**高位运算**和**取模运算**

1. 高位运算

对hashCode进行高位运算的目的是为了减少哈希冲突，提高HashMap的性能。

- 首先，key.hashCode()方法返回的是一个int类型的哈希值，这个哈希值可能会出现哈希冲突，即不同的key可能会产生相同的哈希值。

- 然后，将哈希值h右移16位，得到h的高16位，这个高16位的值可以看作是哈希值的一部分，用于减少哈希冲突。

- 最后，将h的低16位与高16位进行异或运算，得到一个新的哈希值，这个新的哈希值可以更好地分布在HashMap的数组中，减少哈希冲突，提高HashMap的性能。

2. 取模运算

- 首先，n是HashMap的数组长度，hash是键的哈希值。

- 然后，将n-1与hash进行按位与运算，得到的结果是hash在数组中的索引位置i。

由于**n是2的幂次方**，因此n-1的二进制表示中所有位都是1，这样就可以保证按位与运算的结果不会超过数组的长度，即i的值不会越界。

由于n是2的幂次方，因此n-1的二进制表示中除了最高位是1以外，其余位都是0。这样，按位与运算的结果就相当于将hash的二进制表示中除了最高位以外的所有位都取模为n，即i = hash % n。

由于位运算比取模运算更快，因此HashMap使用位运算来实现取模运算，从而提高了HashMap的性能。

`为什么HashMap的容量大小是2的幂次方?`的答案就呼之欲出了。

### 扩容机制

```java
final Node<K,V>[] resize() {
    Node<K,V>[] oldTab = table;
    int oldCap = (oldTab == null) ? 0 : oldTab.length;
    int oldThr = threshold;
    int newCap, newThr = 0;
    // 如果旧的HashMap的数组长度oldCap大于0，说明旧的HashMap已经存在，需要将其扩容
    if (oldCap > 0) {
        // 容量限制 2^30
        if (oldCap >= MAXIMUM_CAPACITY) {
            threshold = Integer.MAX_VALUE;
            return oldTab;
        }
        // oldCap左移1位，即oldCap乘以2
        else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY &&
                    oldCap >= DEFAULT_INITIAL_CAPACITY)
            newThr = oldThr << 1; // double threshold
    }
    // 构造函数初始化 指定容量 
    else if (oldThr > 0) // initial capacity was placed in threshold
        newCap = oldThr;
    // 默认容量16 , threshold = 16*0.75 = 12
    else {               // zero initial threshold signifies using defaults
        newCap = DEFAULT_INITIAL_CAPACITY;
        newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
    }
    // 根据新的HashMap的容量大小newCap和负载因子loadFactor，计算出新的阈值newThr
    if (newThr == 0) {
        float ft = (float)newCap * loadFactor;
        newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ?
                    (int)ft : Integer.MAX_VALUE);
    }
    threshold = newThr;
    @SuppressWarnings({"rawtypes","unchecked"})
    // 将HashMap的数组指向新的Node数组。
    Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];
    table = newTab;
    if (oldTab != null) {
        // 遍历旧的HashMap的数组oldTab，将其中的键值对重新分配到新的HashMap的数组newTab中。对于每个非空的桶oldTab[j]，将其中的键值对重新分配到新的HashMap的数组newTab中。
        for (int j = 0; j < oldCap; ++j) {
            Node<K,V> e;
            if ((e = oldTab[j]) != null) {
                oldTab[j] = null;
                // 如果桶中只有一个键值对，那么直接将这个键值对放到新的HashMap的数组newTab中对应的桶中
                if (e.next == null)
                    newTab[e.hash & (newCap - 1)] = e;
                // 如果桶中的键值对是红黑树节点，那么需要调用TreeNode的split()方法来将这些节点重新分配到新的HashMap的数组newTab中。
                else if (e instanceof TreeNode)
                    ((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
                else { // preserve order
                    Node<K,V> loHead = null, loTail = null;
                    Node<K,V> hiHead = null, hiTail = null;
                    Node<K,V> next;
                    do {
                        next = e.next;
                        // 在将旧的HashMap中的键值对重新分配到新的HashMap的数组中时，需要将键值对按照哈希值的高位来分成两部分，一部分放到原来的桶中，另一部分放到原来的桶加上旧的HashMap的容量大小的位置中
                        if ((e.hash & oldCap) == 0) {
                            if (loTail == null)
                                loHead = e;
                            else
                                loTail.next = e;
                            loTail = e;
                        }
                        else {
                            if (hiTail == null)
                                hiHead = e;
                            else
                                hiTail.next = e;
                            hiTail = e;
                        }
                    } while ((e = next) != null);
                    if (loTail != null) {
                        loTail.next = null;
                        newTab[j] = loHead;
                    }
                    if (hiTail != null) {
                        hiTail.next = null;
                        newTab[j + oldCap] = hiHead;
                    }
                }
            }
        }
    }
    return newTab;
}
```

## get

```java
public V get(Object key) {
    Node<K,V> e;
    return (e = getNode(hash(key), key)) == null ? null : e.value;
}

final Node<K,V> getNode(int hash, Object key) {
    Node<K,V>[] tab; Node<K,V> first, e; int n; K k;
    // 1. 判断table里是否存在元素，不存在直接返回null
    if ((tab = table) != null && (n = tab.length) > 0 &&
        // 1.2 判断 元素的 哈希桶位置 第一个元素不等于空，为空直接返回
        (first = tab[(n - 1) & hash]) != null) {
        if (first.hash == hash && // always check first node
            // 2.1 首先，检查桶中的第一个键值对first，如果它的哈希值和给定的哈希值相等，并且它的键和给定的键相等，那么就找到了对应的键值对，直接返回first。
            ((k = first.key) == key || (key != null && key.equals(k))))
            return first;
        if ((e = first.next) != null) {
            if (first instanceof TreeNode)
                //2.2 如果桶中的第一个键值对是红黑树节点，那么需要调用TreeNode的getTreeNode()方法来查找与给定的键值对匹配的键值对。
                return ((TreeNode<K,V>)first).getTreeNode(hash, key);
            // 2.3 如果桶中有多个键值对，那么需要遍历桶中的所有键值对，查找与给定的键值对匹配的键值对。如果遍历到的键值对的哈希值和给定的哈希值相等，并且它的键和给定的键相），那么就找到了对应的键值对，直接返回
            do {
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    return e;
            } while ((e = e.next) != null);
        }
    }
    return null;
}
```

## remove

```java
public V remove(Object key) {
    Node<K,V> e;
    return (e = removeNode(hash(key), key, null, false, true)) == null ?
        null : e.value;
}


final Node<K,V> removeNode(int hash, Object key, Object value,
                            boolean matchValue, boolean movable) {
    Node<K,V>[] tab; Node<K,V> p; int n, index;
    if ((tab = table) != null && (n = tab.length) > 0 &&
        (p = tab[index = (n - 1) & hash]) != null) {
        Node<K,V> node = null, e; K k; V v;
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            node = p;
        else if ((e = p.next) != null) {
            if (p instanceof TreeNode)
                node = ((TreeNode<K,V>)p).getTreeNode(hash, key);
            else {
                do {
                    if (e.hash == hash &&
                        ((k = e.key) == key ||
                            (key != null && key.equals(k)))) {
                        node = e;
                        break;
                    }
                    p = e;
                } while ((e = e.next) != null);
            }
        }
        if (node != null && (!matchValue || (v = node.value) == value ||
                                (value != null && value.equals(v)))) {
            // 如果键值对是红黑树节点，那么需要调用TreeNode的removeTreeNode()方法来删除节点
            if (node instanceof TreeNode)
                ((TreeNode<K,V>)node).removeTreeNode(this, tab, movable);
            // 如果键值对是桶中的第一个节点，那么直接将桶的引用指向下一个节点。否则，将前一个节点的next指向下一个节点。
            else if (node == p)
                tab[index] = node.next;
            else
                p.next = node.next;
            // 更新HashMap的modCount和size
            ++modCount;
            --size;
            afterNodeRemoval(node);
            return node;
        }
    }
    return null;
}
```