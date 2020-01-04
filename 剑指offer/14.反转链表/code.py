class Solution:
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
         
        p2 = None
        p1 = pHead
         
        while p1!=None:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        return p2
