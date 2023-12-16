def intersection(a, b):
  if len(a) == 0 or len(b) == 0:
    return []
  
  a_dict = {}
  result = []
  for num in a:
    if num in a_dict:
      a_dict[num] += 1
    else:
      a_dict[num] = 1
  
  for each_num in b:
    if each_num in a_dict:
      result.append(each_num)
      a_dict[each_num] -= 1
  
  return result
# can also use set if repeated numbers are not considered.