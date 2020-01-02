class Solution:
    #使用self，把stack1,2当作class的两个属性，pop和push成为两个方法
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
