# 1010

from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) <= 1:
            return 0  # Return 0 if there are not enough elements to form a pair
        
        remainder_count = {}
        result = 0

        for t in time:
            r = t % 60
            complement = (60 - r) % 60  # Find the complement that together with r sums up to 60 (or 0 for a perfect multiple of 60)
            
            # If the complement is already in remainder_count, it means we can form a pair that sums up to a multiple of 60
            if complement in remainder_count:
                result += remainder_count[complement]
            
            # Update the count of this remainder
            if r in remainder_count:
                remainder_count[r] += 1
            else:
                remainder_count[r] = 1
        
        return result
