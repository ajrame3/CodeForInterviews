#528

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)  # get the cumulative sum from given weights
        
        self.total = total


    def pickIndex(self) -> int:
        target = random.uniform(0, self.total) # pick some random number 

        left = 0 
        right = len(self.prefix_sums)

        while left < right: 
            mid = (left + right) // 2 
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()