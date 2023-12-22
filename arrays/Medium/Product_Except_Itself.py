def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    res = [1]*len(nums)

    prefix = 1
    for i in range(0, len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix # multiply here and assignment in prefix
        postfix *= nums[i]
        
    return res