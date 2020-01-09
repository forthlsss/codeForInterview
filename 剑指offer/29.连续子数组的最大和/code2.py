# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum = array[0]
        presum = 0
        for i in array:
            if presum < 0:
                presum = i
            else:
                presum += i
            sum = max(presum,sum)
        return sum
