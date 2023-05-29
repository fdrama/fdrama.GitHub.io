---
title: ArrayList
tags: [source code, java, arrayList, ]
categories: 源码解读
---

## 类关系图

```puml
@startuml

!theme vibrant
top to bottom direction
skinparam linetype ortho

interface Iterable

together{
    interface Collection
    interface List
}

together {
    abstract class AbstractCollection
    abstract class AbstractList
}

together {
    interface Cloneable
    interface RandomAccess
    interface Serializable
}
class ArrayList
Iterable ^-[#008200,dashed]- Collection

List <|-[#008200,plain]- AbstractList
Collection <|-[#008200,plain]- AbstractCollection

Collection <|-[#008200,plain]- List
AbstractCollection <|-[#000082,plain]- AbstractList
AbstractList <|-[#000082,plain]- ArrayList
RandomAccess ^-[#008200,dashed]- ArrayList
Cloneable ^-[#008200,dashed]- ArrayList
Serializable ^-[#008200,dashed]- ArrayList
@enduml
```

## 数据结构

```java
transient Object[] elementData;  // 数组
``` 

### add

### remove

### set

### get