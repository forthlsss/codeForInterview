# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        out = []
        while matrix:
            # 上边界即为数组的第一个子数组
            # 加载第一行
            out += matrix.pop(0)
            # 如果这里仅判断if matrix，那么对于测试数组例[[1],[2],[3]]，循环后变成了[[],[]]，matrix不为空
            if matrix and matrix[0]:
                # 右边界即为数组每一项的最后一个元素
                for row in matrix:
                    # 加载每一行的最后一个
                    out.append(row.pop())
            # 下边界即为数组最后一个子数组的逆序排列
            if matrix:
                #倒序加载最后一行
                out += matrix.pop()[::-1]
            if matrix and matrix[0]:
                # 左边界即为数组从尾到头的每一项子数组的第一个元素
                for row in matrix[::-1]:
                    #倒序加载第一列
                    out.append(row.pop(0))
        return out
