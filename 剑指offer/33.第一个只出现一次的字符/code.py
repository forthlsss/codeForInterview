# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        location_dict = {}
        index_list = []
        for i in range(len(s)):
            if s[i] not in location_dict:
                location_dict[s[i]]=i
                index_list.append(s[i])
            else:
                if s[i] in index_list:
                    index_list.remove(s[i])
        if index_list:
            return location_dict[index_list[0]]
        else:
            return -1
