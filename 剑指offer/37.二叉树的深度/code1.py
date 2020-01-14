# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue = [pRoot]
        depth = 0
        while queue:
            sum = len(queue)
            for i in range(sum):
                res = queue.pop(0)
                if res.left:
                    queue.append(res.left)
                if res.right:
                    queue.append(res.right)
            depth+=1
        return depth
