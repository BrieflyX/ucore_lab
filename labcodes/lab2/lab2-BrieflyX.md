# Lab2 Report
# 裴中煜 2012010685

## 练习1

first-fit的实现主要由以下几个部分组成

1. 初始化
初始化时，在default_init_memmap中需要建立起一张内存页的链表，将每页的对应部分（如flags、property等）设置好，通过list_add_before将它们都加入到链表中。并将ref置为0.设置全局变量nr_free为n，现在内存为一整块，故头部base存放的元数据property设置为n。

2. 分配alloc
从free_list的位置开始遍历整个链表，每遇到一个节点就检查property值，如果有大于需要的n的节点，则从这个节点开始，其后n个节点对应的页都将被分配出去，具体即为调用SetPageReserved与ClearPageProperty，然后将此页从链表中删除。如果这一块分配完之后还剩下一些空间，则需要设置留在链表中的节点的property值，让它作为新的一块的头部。同时总节点数减n

3. 释放free
仍然需要从free_list的位置开始遍历整个链表，直到找到比需要释放的页base地址恰好大一点的节点p，然后将base以及其后n个页插入链表中p前面的位置。同时与初始化一样需要设置base的一些属性值。接着需要做的工作即为合并，向上合并的操作比较容易，只需要比较刚刚找到的插入点p的地址是不是与base+n一样，如果相等则2块是相连的，就可以把p的property值加到base上，同时将p的property置0.向下合并比较麻烦，首先需要判断base前一个节点的地址是否与base相接，如果相接则是相邻的块，这样需要连续向前遍历直到找到property不为0的节点即为前一个块的头部，类似地，可以将base的property加到前一块上。

4. 改进空间
上述的实现方法问题在于对块的分配和释放都需要进行O(n)次操作进行插入，改进的方法可以在节点中增加一项，每个块的头部节点指向其尾部节点，尾部节点指向头部节点。这样在分配时不需要释放n次，只需要解除头尾节点即可，而在释放时插入也可以直接将头尾节点接入链表中因为中间的节点都已经保持着原来的链接关系。而在合并时也不需要向前遍历找到头部，直接从前一块的尾节点就可以找到头结点。

## 练习2

1. 页目录表项和页表项各个标志位

```
#define PTE_P           0x001                   // 是否使用中，已用于页机制中。
#define PTE_W           0x002                   // 是否可写，已用于页机制中。
#define PTE_U           0x004                   // 用户态使用，用于用户态管理。
#define PTE_PWT         0x008                   // 是否写直达，用于cache的写回。
#define PTE_PCD         0x010                   // 禁用cache，用于cache系统。
#define PTE_A           0x020                   // Accessed
#define PTE_D           0x040                   // 脏位，被改写，用于write-back写回cache。
#define PTE_PS          0x080                   // Page Size
#define PTE_MBZ         0x180                   // 保留位，全部置0
#define PTE_AVAIL       0xE00                   // 软件是否可以使用
```

2.

## 练习3

