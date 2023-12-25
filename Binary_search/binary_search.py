class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            mid = (first + last ) // 2
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                return mid
        
        return -1