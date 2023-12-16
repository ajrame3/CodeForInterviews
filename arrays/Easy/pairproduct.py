def pair_product(numbers, target_product):
  if len(numbers) == 0:
    return (-1, -1)
  
  nums_dict = {}
  for i in range(len(numbers)):
    if target_product % numbers[i] == 0:
      res = target_product // numbers[i]
      if res in nums_dict:
        return (nums_dict[res], i)
      else:
        nums_dict[numbers[i]] = i
  