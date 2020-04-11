class Solution_max_96_num:
  def maximum96Number (self, num):
    num_str = str(num)
    len_num_str = len(num_str)
    for i in range(0,len_num_str):
      if num_str[i] == '6':
        num_str = num_str[0:i]+'9'+num_str[(i+1):len_num_str]
        break
    return int(num_str)