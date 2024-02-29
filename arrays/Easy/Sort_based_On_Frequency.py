class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each element
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        print(counts)
        # Step 2: Sort the elements based on their frequencies
        sorted_nums = sorted(nums, key=lambda x: (counts[x], -x))
        return sorted_nums