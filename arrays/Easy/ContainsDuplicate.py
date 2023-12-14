class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return -1
        
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        
        return False