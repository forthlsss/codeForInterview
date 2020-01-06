#思路没问题,但是数组的操作要注意,res全部pop完以后再切片就会报错,所以要加一个判断res是否有元素
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        res = []
        while pushV:
            res.append(pushV.pop(0))
            # 加一个while res
            while res and res[-1]==popV[0] and res:
                res.pop()
                popV.pop(0)
        if not res:
            return True
