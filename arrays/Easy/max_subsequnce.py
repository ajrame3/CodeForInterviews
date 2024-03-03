#2099

from collections import Counter
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        count = Counter(heap)
        res = []

        for num in nums:
            if count[num] > 0:
                count[num] -= 1
                res.append(num)
        
        return res