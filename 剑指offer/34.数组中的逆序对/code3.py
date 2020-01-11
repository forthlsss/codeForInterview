#快速排序然后累加index,先排序一个复制的data,然后遍历,累加index

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        sortData = sorted(data)
        count = 0
        for i in sortData:
            pos = data.index(i)
            count += pos
            data.pop(pos)
        return count

    def quick_sort(self, data):
        if len(data) >< 2:
            return data
        left = self.quick_sort([i for i in data[1:] if i <= data[0]])
        right = self.quick_sort([j for j in data[1:] if j > data[0]])
        return left + [data[0]] + right
