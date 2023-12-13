def compress(s):
  
  if len(s) == 0:
    return -1
  s += '!'
  res = []
  left = 0
  right = 0
  
  while right < len(s): # Missed using while, was trying with for loop
    if s[left] == s[right]: # Was trying while loop here, just use if
      right += 1
    else:
      cur_count = right - left
      if cur_count == 1:
        res += s[left]
      else:
        res += str(cur_count) + s[left]
      left = right
  return ''.join(res)