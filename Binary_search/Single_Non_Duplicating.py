class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r: # Take care no '=' here
            mid = (l+r) // 2
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] != nums[mid + 1]:
                r = mid
            else:
                l = mid + 2 # Important 
        
        return nums[l]
        