# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = [root]
        l = []
        while res:
            a = res.pop(0)
            l.append(a.val)
            if a.left:
                res.append(a.left)
            if a.right:
                res.append(a.right)
        return l
