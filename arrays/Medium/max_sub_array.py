class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return -1
        
        max_value = -sys.maxsize-1
        res = 0

        for num in nums:
            res += num

            if res > max_value:
                max_value = res
            
            if res < 0:
                res = 0
        
        return max_value