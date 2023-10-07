---
title: array
tags: [array]
categories: datastructure
---

## array 介绍

数组（Array）：是一种线性表数据结构。它用一组连续的内存空间，数组是相同类型数据的集合。

数组中特定数据点的位置被称为其索引，而数据本身被称为元素。数组的索引通常是从 0 开始。

![Alt text](../../images/datastructure/array.png)

## array 特点

- 数组大小固定：数组的大小是固定的，无法动态扩容。
- 同类型元素：数组中的数据类型必须相同，否则无法通过下标计算偏移量。
- 内存连续：数组中的元素在内存中是连续存储的，可以通过下标计算偏移量，查找效率高。
- 下标访问：数组支持随机访问，通过下标访问元素的时间复杂度为 O(1)，从0开始。

## array 使用

数组定义语法：`type [] name`; 或者 `type name []`;

```java
int[] arr; // 声明数组变量 dataType [ ] nameOfArray; 
arr = new int[10]; // 创建数组，分配内存空间，初始化默认值，arr指向数组的首地址
```

## 初始化

### 静态初始化

初始化时只指定数组长度，由系统为数组分配初始值。

```java
int[] arr = {1, 2, 3, 4, 5};
```

### 动态初始化

初始化时指定每个数组元素的初始值，由系统决定数组长度

```java
int[] arr = new int[10];
```

### 多维数组

多维数组本质上也是一维数组，其每个元素是一个子数组的引用。 `dataType[][] arrayName = new dataType[row][column];`

![Alt text](../../images/datastructure/mulitarray.png)

```java
String[][] str = new String[3][4];
```

#### 应用场景

1. 矩阵运算
2. 图像处理
3. 游戏地图
4. 地理信息存储
