#848

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        res = []
        if len(shifts) == 0 or len(s) == 0:
            return s

        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        
        for i in range(len(s)):
            new_char = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
            res.append(new_char)
        
        return ''.join(res)