# 921

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        l_count = r_count = added = 0

        for char in s:
            if char == "(":
                l_count += 1
            else:
                if r_count < l_count:
                    r_count += 1
                else:
                    added += 1
        
        added += l_count - r_count

        return added

'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        clo = 0
        ope = 0
        for i in s:
            if i == '(':
                ope += 1
            if i == ')':
                if ope > 0:
                    ope -= 1
                else:
                    clo += 1
        return clo + ope

'''
        