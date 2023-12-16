'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 
'''

def sort_colors(nums):
    # This is dutch national flag problem
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high =- 1

# Another technique is:

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Looked at counting sort algorithm
        Based on counting sort algorithm,

        Created frequency count of each num(color)
        Just implemented the Counting Sort step by step
        """
        #Time Complexity --> O(n)
        #Time taken to implment : 50 minutes
        
        if len(nums) == 0 or len(nums) == 1:
            return nums

        freq_hash = [0] * (len(nums) + 1)

        for num in nums:
            freq_hash[num] += 1
        
        for i in range(1, len(freq_hash)):
            freq_hash[i] = freq_hash[i - 1] + freq_hash[i]
        
        res = [None] * len(nums)

        for from_last in reversed(nums):
            res[freq_hash[from_last] - 1] = from_last
            freq_hash[from_last] -= 1
        
        nums[:] = res
    

