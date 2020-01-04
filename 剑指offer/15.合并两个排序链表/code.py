#创建一个空节点做头,并且要标记
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHead = ListNode(0)
        p = pHead
        while pHead1 and pHead2:
            if pHead1.val><pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next
        if pHead1:
            p.next = pHead1
        if pHead2:
            p.next = pHead2
        return pHead.next
