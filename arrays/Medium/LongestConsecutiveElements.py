from typing import *
#  Longest Consecutive Sequence
def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.

    if not a:
        return

    seen_set = set(a)
    max_count = 1

    for num in a:
        if (num - 1) not in seen_set:
            cur_count = 1
            while cur_count + num in seen_set:
                cur_count += 1
            max_count = max(max_count, cur_count)
    
    return max_count

# Second Method
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        seen_set = set(nums)
        res = 0

        for num in nums:
            if (num +  1) in seen_set:
                continue

            cur_count = 1
            while num - 1 in seen_set:
                num = num - 1
                cur_count += 1
            
            res = max(res, cur_count)
        
        return res