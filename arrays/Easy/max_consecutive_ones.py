import sys

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)
        max_one = -sys.maxsize - 1
        temp_res = 0

        for i in range(n):
            if nums[i] != 1:
                max_one = max(max_one, temp_res)
                temp_res = 0
            else:
                temp_res += 1
        
        return max(max_one, temp_res)