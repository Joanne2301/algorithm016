﻿学习笔记

第五课：哈希表，映射，集合
1. 哈希在python中的实现方式主要是dict（map）和set；
2. 哈希函数和哈希表的概念要区分开，哈希函数可以有很多种，最简单的例子有取模；
3. 哈希碰撞要尽可能避免，通过选择合适的哈希函数避免，或尽可能平均每个地址碰撞的概率；

第六课：树，二叉树，二叉搜索树
1. 树只是一种数据结构，最基本的树是无序的，树结构的实现是基于递归；
2. 二叉树是树的一种应用形式，有定义好的属性，属性是针对所有节点而不是单个节点，具有重复性；

第七课：堆，二叉堆
1. 堆要满足其定义：可以以O（1）的时间复杂度找到最大/最小值的数据结构；二叉堆只是堆的一种实现方式，堆不等于二叉堆；
2. 工业上常用的是斐波那契堆，实现相对复杂；相比之下二叉堆性能不理想，但较好理解和实现，面试常常出现；
3. 二叉堆通过完全二叉树实现，因此有固定规律，实现方式仅需要一维数组，通过索引和二叉堆的规律，即父亲节点与子节点之间的索引关系实现定位；
4. 二叉堆的插入操作：新元素先插入堆的尾部，依次向上调整结构（HeapifyUp）- O（logN）
5. 二叉堆的删除操作：将堆尾元素替换到堆顶（欲删除元素的位置），从堆顶（删除元素位置）依次向下调整（HeapifyDown） - O（logN）
6. 使用二叉堆可以直接调用优先队列的接口
7. 图的二维实现：adjacency matrix/list
8. 图算法（DFS，BFS注意一定要加visited，因为树是不会重复visit的，但是图会）