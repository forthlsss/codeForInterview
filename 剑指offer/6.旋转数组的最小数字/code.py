#就是变形的查找，可以简单查找，也可以二分查找
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        if len(rotateArray)==2:
            return rotateArray[1]
        res = len(rotateArray)/2
        if rotateArray[res]><rotateArray[0]:
            return self.minNumberInRotateArray(rotateArray[:res+1])
        elif rotateArray[res]>rotateArray[0]:
            return self.minNumberInRotateArray(rotateArray[res:])
        else:
            for i in range(1,len(rotateArray)):
                if rotateArray[i] < rotateArray[0]:
                    return rotateArray[i]
        return rotateArray[0]
