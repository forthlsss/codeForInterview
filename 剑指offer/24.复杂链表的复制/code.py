# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # 返回 RandomListNode
        if not pHead:
            return None
         
        p = pHead
        # first step, N' to N next
        while p:
            pnext = p.next
            copynode = RandomListNode(p.label)
            copynode.next = pnext
            p.next = copynode
            p = pnext
        
        p = pHead
        
        # second step, random' to random'
        while p:
            copyp = p.next
            if p.random: 
                copyp.random = p.random.next
            p = copyp.next
            
        p = pHead    
        # third step, split linked list
        copyHead = pHead.next
        while p:
            copynode = p.next
            pnext = copynode.next
            p.next = pnext
            if pnext:
                copynode.next = pnext.next
            else:
                copynode.next = None
            p = pnext
        return copyHead
