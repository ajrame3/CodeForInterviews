class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        
        class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # lowest must be on left side of mid 
            if nums[mid] < nums[r]:
                r = mid
            # lowest must be on right side of mid
            else:
                l = mid + 1
        return nums[l]
