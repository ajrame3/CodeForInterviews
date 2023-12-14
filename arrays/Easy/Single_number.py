def single_number(nums):

    if len(nums) == 0:
        return -1
    
    num_dict = {}

    for i in range(len(nums)):
        if nums[i] in num_dict:
            num_dict[nums[i]] += 1
        else:
            num_dict[nums[i]] = 1
    
    for key, value in num_dict.itmes():
        if value == 1:
            return key
        
    
    return -1
