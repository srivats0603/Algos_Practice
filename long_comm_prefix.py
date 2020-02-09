class Solution_lcp():
  def __init__(self):
    pass
  
  def longestCommonPrefix(self, strs):
    num_strings = len(strs)
    print("total strings to compare ={}".format(num_strings))
    str_dict = {}
    if num_strings == 0:
      return ""
    if num_strings == 1:
      return strs[0]
    str_len_dict = {}
    for i in range(0,num_strings):
      str_len_dict[i] = len(strs[i])
      if str_len_dict[i] == 0:
        return ""
  
    len_common_prefix = 0
    common_char_dict = {}
    for i in range(0,min(str_len_dict[0],str_len_dict[1])):
      if strs[0][i] == strs[1][i]:
        len_common_prefix = len_common_prefix+1
        common_char_dict[i] = strs[0][i]
      else:
        break
    if len_common_prefix == 0:
      return ""
    if num_strings == 2:
      return strs[0][0:len_common_prefix]
    else:
      for i in range(2,num_strings):
        for key in range(0,min(str_len_dict[i],len_common_prefix)):
          if strs[i][key] == common_char_dict[key]:
            len_common_prefix = key+1
          else:
            if key == 0:
              len_common_prefix = 0
            break
      if len_common_prefix == 0:
        return ""
      elif len_common_prefix > 0: 
        return strs[0][0:len_common_prefix]