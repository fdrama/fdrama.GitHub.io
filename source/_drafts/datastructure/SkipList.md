---
title: skip list
tags: [skip list]
categories: datastructure
---

## skip list 介绍

跳表（Skip List）：是一种随机化的数据结构，实质上是一种可以进行二分查找的**有序链表**。跳表的出现是为了弥补链表只能顺序查找的缺陷，它通过构建**多级索引**来提高查询效率，实现了基于链表的“二分查找”。

## skip list 特点

- 跳表是一种动态数据结构，支持快速地插入、删除、查找操作，时间复杂度都是 O(logn)。
- 跳表对标的是平衡树（AVL Tree），AVL Tree 的插入、删除、查找操作的时间复杂度也是 O(logn)，且实现比较复杂，而跳表的实现比较简单。
- 跳表的实现很灵活，可以通过改变索引构建策略来调整性能。
- 跳表的缺点是维护成本较高，每次插入、删除操作都要维护索引，空间复杂度是 O(n)。
- 跳表的效率与索引的构建有很大关系，如果索引的构建不合理，很可能导致跳表退化成单链表，时间复杂度就退化成 O(n)。

## 跳表的实现

### 数据结构

```java
public class SkipList<K extends Comparable<K>, V> {

    private static final int MAX_LEVEL; // 最大层数
    private int level; // 当前层数
    private Node<K, V> head; // 头节点
    private Random random; // 随机方法

}
```

### 跳表的插入

1. 查询

跳表（Skip lists）是通过一种称为“抛硬币”的技术来实现的。每次插入操作都会生成一个随机数，以确定新元素将占据的层数。这意味着平均而言，每个元素将在底层中占据log(n)层，其中n是底层中的元素数量。

## skip list 应用

### Redis 中的有序集合

- Redis 中的有序集合（Sorted Set）就是用跳表来实现的。
- ConcurrentSkipListMap
- ConcurrentSkipListSet

## 参考资料

- [跳表（Skip List）](https://lotabout.me/2018/skip-list/)
- [Skip List (Introduction)](https://www.geeksforgeeks.org/skip-list/)
- [baeldung skiplists](https://www.baeldung.com/cs/skip-lists)