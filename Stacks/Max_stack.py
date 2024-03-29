class MaxStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return max(self.stack)
        

    def popMax(self) -> int:
        val = self.peekMax()
        for i in range(-1, -len(self.stack) - 1, -1):
            if val == self.stack[i]:
                del self.stack[i]
                break
        
        return val

        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()