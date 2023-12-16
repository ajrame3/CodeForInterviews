class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        n = len(nums)

        nums_dict = {}

        for i in range(n):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        
        for key, value in nums_dict.items():
            if value > (n // 2):
                return key
    
        return -1