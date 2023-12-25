class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # important - just return left index to say where to insert if not found

        left = 0
        right  = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right  = mid - 1
            else:
                return mid
        
        return left