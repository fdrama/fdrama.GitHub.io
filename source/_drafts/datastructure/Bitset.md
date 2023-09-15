---
title: bitset
tags: [bitset]
categories: datastructure
---

## bitset 介绍

位图（Bitset）：用于表示二进制位的数据结构，通常用于高效地存储大量布尔值。通过使用位数组来存储大量数据，其中每个位代表一个布尔值（0或1）。这种表示方式允许非常紧凑地存储大量布尔值，因为每个位只占用一个比特（1位），而不是一个字节（8位）或更多的字节。这使得 `BitSet` 在存储大规模布尔数据时非常高效。

## bitset 应用

### 布隆过滤器

布隆过滤器（Bloom Filter）：是一种空间效率很高的随机数据结构，它利用位数组很简洁地表示一个集合，并能判断一个元素是否属于这个集合。

布隆过滤器的原理是：当一个元素被加入集合时，通过K个散列函数将这个元素映射成一个位数组中的K个点，把它们置为1。检索时，我们只要看看这些点是不是都是1就（大约）知道集合中有没有它了：如果这些点有任何一个0，则被检元素一定不在；如果都是1，则被检元素很可能在。这就是布隆过滤器的基本思想。

布隆过滤器的优点是空间效率和查询时间都远远超过一般的算法，缺点是有一定的误识别率和删除困难。

```java
import java.util.BitSet;
import java.util.function.Function;

public class BloomFilter<T> {
    private final BitSet bitSet;
    private final int numHashFunctions;
    private final Function<T, Integer>[] hashFunctions;

    public BloomFilter(int expectedSize, double falsePositiveRate) {
        // 计算位数组大小
        int numBits = (int) (-expectedSize * Math.log(falsePositiveRate) / Math.pow(Math.log(2), 2));
        bitSet = new BitSet(numBits);

        // 计算哈希函数数量
        numHashFunctions = (int) (numBits / expectedSize * Math.log(2));

        // 创建哈希函数
        hashFunctions = new Function[numHashFunctions];
        for (int i = 0; i < numHashFunctions; i++) {
            int seed = i;
            hashFunctions[i] = (T element) -> {
                int hash = element.hashCode();
                hash ^= (hash >>> 20) ^ (hash >>> 12);
                return (hash ^ (hash >>> 7) ^ (hash >>> 4)) & (numBits - 1);
            };
        }
    }

    public void insert(T element) {
        for (Function<T, Integer> hashFunction : hashFunctions) {
            int index = hashFunction.apply(element);
            bitSet.set(index, true);
        }
    }

    public boolean contains(T element) {
        for (Function<T, Integer> hashFunction : hashFunctions) {
            int index = hashFunction.apply(element);
            if (!bitSet.get(index)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        BloomFilter<String> bloomFilter = new BloomFilter<>(1000, 0.01);

        // 插入元素
        bloomFilter.insert("item1");
        bloomFilter.insert("item2");
        bloomFilter.insert("item3");

        // 检查元素是否存在
        System.out.println(bloomFilter.contains("item1")); // true
        System.out.println(bloomFilter.contains("item4")); // false (可能的误判)
    }
}

```
