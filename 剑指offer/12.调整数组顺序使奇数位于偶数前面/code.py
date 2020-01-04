#牛客上通不过的实例本地没问题
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        length = len(array)
        p1 = 0
        p2 = length-1
        while p1<p2:
            while array[p1]%2!=0:
                p1+=1
            while array[p2]%2==0:
                p2-=1
            if p1><p2:
                array[p1],array[p2]=array[p2],array[p1]
                p1+=1
                p2-=1
        return array
