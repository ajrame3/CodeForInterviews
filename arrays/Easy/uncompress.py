def uncompress(s):
  if len(s) == 0:
    return None
  
  str_num = ''
  res_num = 0
  result = ''
  
  for each_char in s:
    if each_char.isdigit():
      str_num += each_char
      res_num = int(str_num)
    else:
      result = result + (each_char * res_num)
      str_num = ''
      res_num = 0
  
  return result