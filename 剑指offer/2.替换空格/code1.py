#1.新空间
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = ''
        b = '%20'
        for i in s:
            if i ==' ':
                new_s+=b
            else:
                new_s+=i
        return new_s
