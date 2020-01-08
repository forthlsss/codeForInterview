# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        if len(numbers)==1:
            return numbers[0]
        res = numbers[0]
        amount = 1
        for i in numbers[1:]:
            if res == i:
                amount+=1
            else:
                amount-=1
                if amount==0:
                    res = i
                    amount=1
        amount = 0
        for i in numbers:
            if res==i:
                amount+=1
        if amount>len(numbers)/2:
            return res
        else:
            return 0 

注:\
[1,2,3,2,4,2,5,2,3]\
最后一定会得到一个res,还需要统计一下res的数量,判断是否为大于一半的
