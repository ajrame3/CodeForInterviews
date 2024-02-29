#697
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        freq = {}
        left = {}
        right = {}
        degree = 0
        res = len(nums)
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
            degree = max(degree, freq[nums[i]])

            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
        
        for num, frequncy in freq.items():
            if frequncy == degree:
                res = min(res, right[num] - left[num] + 1)
        
        return res




        