# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k><=0:
            return None
        res = 0
        p = q = head
        while res<k-1 and q:
            q = q.next
            res+=1
        if q is None:
            return None
        while q.next:
            q = q.next
            p = p.next
        return p
