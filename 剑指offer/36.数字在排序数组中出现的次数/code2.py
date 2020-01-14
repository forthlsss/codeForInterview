# -*- coding:utf-8 -*-
class Solution:
    def getleft(self,data,k,left,right):
        while left <= right:
            mid = (left + right) //2
            if data[mid] >= k:  
    # 注意，传统的二分法没有等号，如果相等了，就直接返回mid了，但是这个有点特殊
                right = mid -1
            else:
                left = mid +1
        return left
    # 找data中最后一次出现k的下标
    def getright(self,data,k,left,right):
        while left <= right:
            mid = (left + right) //2
            if data[mid] > k:
                right = mid -1  
            else: # 注意
                left = mid +1
        return right
    def GetNumberOfK(self, data, k):
        # write code here
        left = 0
        right = len(data)-1
        rightk = self.getright(data,k,left,right)
        leftk = self.getleft(data,k,left,right)
        return  rightk - leftk  + 1
