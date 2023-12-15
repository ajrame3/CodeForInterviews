def most_frequent_char(s):
  
  if len(s) == 0:
    return -1
  
  dict_s = {}
  for each in s:
    if each in dict_s:
      dict_s[each] += 1
    else:
      dict_s[each] = 1
  
  max_value = 0
  most_freq = ''
  for key, value in dict_s.items():
    if value > max_value:
      max_value = value
      most_freq = key
  
  return most_freq