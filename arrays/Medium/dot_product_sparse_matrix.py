# 1570

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0

        for i in range(len(vec.nums)):
            if self.nums[i] != 0 and vec.nums[i] != 0:
                dot_product += (self.nums[i] * vec.nums[i])
        
        return dot_product
            

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
    
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []

        for i, num in enumerate(nums):
            if num:
                self.nums.append((i, num))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0

        i = j = 0

        while i < len(self.nums) and j < len(vec.nums):
            index_i, num_i = self.nums[i]
            index_j, num_j = vec.nums[j]

            if index_i == index_j:
                dot_product += (num_i * num_j)

                i += 1
                j += 1

            elif index_i > index_j:
                 j += 1
            else:
                i += 1
        
        return dot_product
            

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)