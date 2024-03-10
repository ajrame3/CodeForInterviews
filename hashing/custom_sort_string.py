# 791

from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        alpha_dict = defaultdict(int)
        others = ""

        for char in s:
            if char in order:
                alpha_dict[char] += 1
            else:
                others += char
        
        new_s = ""

        for c in order:
            if c in alpha_dict:
                new_s += c * alpha_dict[c]
        
        return new_s + others


        