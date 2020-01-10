# -*- coding:utf-8 -*-
class Solution:
    def compare(self,num1,num2):
        t = str(num1)+str(num2)
        s = str(num2)+str(num1)
        if t>s:
            return 1
        elif t<s:
            return -1
        else:
            return 0
    def PrintMinNumber(self,numbers):
        if not numbers:
            return ''
        tmpNumbers = sorted(numbers,cmp=self.compare)
        return int(''.join(str(x) for x in tmpNumbers))
