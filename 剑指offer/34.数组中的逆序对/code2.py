# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        res = max(data)
        tmp = min(data)
        sum = 0
        while tmp<res:
            sum+=data.index(tmp)
            data.remove(tmp)
            tmp = min(data)
        return sum
