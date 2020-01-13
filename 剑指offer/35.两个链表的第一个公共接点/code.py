# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here

        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        tmp = None
        while stack1 and stack2:
            if stack1[-1]==stack2[-1]:
                tmp = stack1.pop()
                stack2.pop()
            else:
                break
        return tmp
```
