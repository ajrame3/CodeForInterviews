#2817

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))

        min_heap = [] # min_heap is a min heap for (idx, val) pairs
        max_heap = [] # max_heap is a max heap for (idx, val) pairs
        min_diff = float('inf') # keeps track of the minimum absolute differencce

        for val, idx in sorted_nums:
            heapq.heappush(min_heap, (idx, val))
            heapq.heappush(max_heap, (-idx, val))

            # smallest index in the heap (i.e. the root) is more than x away from idx
            while len(min_heap) > 0 and min_heap[0][0] <= idx - x:
                min_diff = min(min_diff, val - heapq.heappop(min_heap)[1])
            
            # largest index in the heap (i.e. the root) is more than x away from idx
            while len(max_heap) > 0 and max_heap[0][0] <= -(x + idx):
                min_diff = min(min_diff, val - heapq.heappop(max_heap)[1])
        
        return min_diff

        