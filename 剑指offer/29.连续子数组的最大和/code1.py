#(有问题,但是网上能通过)
#记录的时候发现有问题
#第一遍自己写的,容易漏情况

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array)==1:
            return array[0]
        sum = 0
        mark = 0
        for i in array:
            sum+=i
            if sum<0:
                sum = 0
        #如果sum>0,还要加上最后可能有的负数,这里就有问题,如果有[-6,1,-2],到1就停了,还应该往前
        if sum>0:
            for j in array[::-1]:
                if j < 0:
                    sum-=j
                else:
                    break
            return sum
        else:
            return max(array)
