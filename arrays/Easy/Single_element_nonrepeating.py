class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return -1
        
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map:
                num_map[nums[i]] += 1
            else:
                num_map[nums[i]] = 1
        
        for key, value in num_map.items():
            if value == 1:
                return key

        return -1

## Can also be done using XOR methodology
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor