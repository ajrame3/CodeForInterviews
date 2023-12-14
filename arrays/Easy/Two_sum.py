class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return 0
        
        seen = {}

        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in seen:
                return [seen[other_num], i]
            else:
                seen[nums[i]] = i
        
        return [-1, -1]