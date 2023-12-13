class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        orig_sum = n * (n + 1) // 2
        sum_given = sum(nums)

        return int(orig_sum - sum_given)