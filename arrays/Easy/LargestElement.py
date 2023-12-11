def max_value(nums):
  
  if len(nums) == 0:
    return None
  
  if len(nums) == 1:
    return nums[0]
  
  result = nums[0]
  
  for i in range(len(nums)):
    if result < nums[i]:
      result = nums[i]
    
  return result