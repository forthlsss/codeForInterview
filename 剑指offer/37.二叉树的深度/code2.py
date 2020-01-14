class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        lDepth = self.TreeDepth(pRoot.left)
        rDepth = self.TreeDepth(pRoot.right)
        return max(lDepth,rDepth)+1
