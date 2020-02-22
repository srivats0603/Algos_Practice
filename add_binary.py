class Solution_addBinary: 
  def addBinary(self, a, b):
    len_a = len(a)
    len_b = len(b)
    if (len_a == 0):
      return b
    if (len_b == 0):
      return a
    if len_a>len_b:
      long_str = a
      len_short_str = len_b
    else:
      long_str = b
      len_short_str = len_a
    return_binary = ""
    carry_over = 0
    i = 0
    while i < len_short_str:
      i = i+1
      this_sum = int(a[len_a-i])+int(b[len_b-i])+carry_over
      if this_sum < 2:
        return_binary = str(this_sum)+return_binary
        carry_over = 0
      elif this_sum == 2:
        return_binary = "0"+return_binary
        carry_over = 1
      elif this_sum == 3:
        return_binary = "1"+return_binary
        carry_over = 1
    temp_len = len(long_str) - len_short_str
    if carry_over == 0:
      return_binary = long_str[0:temp_len]+return_binary
    else:
      return_binary = self.addBinary(long_str[0:temp_len],"1")+return_binary
    return return_binary