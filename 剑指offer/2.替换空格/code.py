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
```
```
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #字符串不能直接修改和添加,所以要先转为list 
        s = list(s)
        blank = s.count(' ')
        lenght = len(s)
        s += [0]*2*blank
        new_len = len(s)
        while lenght:
            if s[lenght-1]==' ':
                s[new_len-1]='0'
                s[new_len-2]='2'
                s[new_len-3]='%'
                new_len-=3
            else:
                s[new_len-1]=s[lenght-1]
                new_len-=1
            lenght-=1
        #把list重新转为字符串
        s = ''.join(s)
        return s
```
