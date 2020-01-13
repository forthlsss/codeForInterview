# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        return self.search(data,k+0.5)-self.search(data,k-0.5)
    def search(self,data,num):
        left = 0
        right = len(data)-1
        while left<=right:
            mid = (left+right)/2
            if data[mid]>num:
                right = mid-1
            else:
                left = mid+1
        return right
