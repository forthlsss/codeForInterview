#?好像很简单
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, ListNode):
        # write code here
        if not ListNode:
            return []
        res = []
        while ListNode:
            res.append(ListNode.val)
            ListNode = ListNode.next
        return res[::-1]
