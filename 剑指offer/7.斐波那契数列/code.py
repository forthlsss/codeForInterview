#递归很简单，也可以用迭代
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        res = [0,1,1,2]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]
        # write code here
