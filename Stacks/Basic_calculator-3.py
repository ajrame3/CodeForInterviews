class Solution:
    def calculate(self, s: str) -> int:

        num = 0
        op = "+"

        stack = []

        def helper(op, num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            elif op == "/":
                stack.append(int(stack.pop()/ num))
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "(":
                stack.append(op)
                num = 0
                op = "+"
            elif s[i] in ["+", "-", "*","/", ")"]:
                helper(op, num)
                if s[i] == ")":
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    helper(op, num)
                num = 0
                op = s[i]
        
        
        helper(op, num)
        return sum(stack)


from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        q=deque(s.replace(' ',''))
        return self.helper(q)
    
    def helper(self,q):
        stack = []
        num=''
        sign='+'
        
        while q:
            x=q.popleft()
            if x=='(':
                num=self.helper(q)
            if x.isnumeric():
                num += x
            if not x.isnumeric() or not q:
                if sign =='+':
                    stack.append(int(num or 0))
                elif sign =='-':
                    stack.append(-1*int(num or 0))
                elif sign == '*':
                    stack.append(stack.pop()*int(num) )
                elif sign == '/':
                    stack.append(int(stack.pop()/int(num)))
                sign = x
                num = ''
            if x== ')':
                break
        
        return sum(stack)   