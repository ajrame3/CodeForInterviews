class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]
    '''
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
    
    '''    
    
    
    def binary_search(self, nums, target, findinleft):

        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                if findinleft:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return index
        


        