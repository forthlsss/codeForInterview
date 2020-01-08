# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.perm(ss,res,'')
        uniq = list(set(res))
        return sorted(uniq)
    def perm(self,ss,res,path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],res,path+ss[i])
