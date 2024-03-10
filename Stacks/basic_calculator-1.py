# 224

class Solution:
    def calculate(self, s: str) -> int:

        cur_num = 0
        sign = 1
        res = 0
        stack = []

        for char in s:
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char in ['+', '-']:
                res += sign * cur_num
                sign = 1 if char == '+' else -1
                cur_num = 0
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif char == ")":
                res += sign * cur_num
                res *= stack.pop()
                res += stack.pop()
                cur_num = 0
        
        return res + sign * cur_num


        