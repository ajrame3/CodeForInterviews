#2384

import collections


class Solution:
    def largestPalindromic(self, num: str) -> str:

        digit_counts = collections.Counter(num)
        first_half = []
        center = ""

        for digit in range(9, -1, -1):
            digit_char = str(digit)
            if digit_char in digit_counts:
                digit_count = digit_counts[digit_char]

                num_pairs = digit_count // 2

                if num_pairs:
                    if not first_half and not digit:
                        digit_counts["0"] = 1
                    else:
                        first_half.append(digit_char * num_pairs)
                
                if digit_count % 2 and not center:
                    center = digit_char
        
        if not center and not first_half:
            return "0"
        
        return "".join(
            first_half + [center] + first_half[::-1]
        )
        
        
        