1.迭代
```
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
         
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        
        p = pRootOfTree
        stack = []
        resStack = []
        #先从根节点向左把一路的左节点进栈,然后依次pop(),得到的就是最小的一个节点,先把这个节点进resStack如果得到的节点有右节点,则指向右节点,再将他的左节点进栈,依次就能得到排序数组
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                res = stack.pop()
                resStack.append(res)
                p = res.right
                
        headNode = resStack[0]
        while resStack:
            node = resStack.pop(0)
            #串成双向链表
            if resStack:
                node.right = resStack[0]
                resStack[0].left = node
        return headNode
```
2.递归
