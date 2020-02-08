class Solution_ls():
  def __init__(self):
    pass
  def lengthOfLongestSubstring(self,s):
    len_s = len(s)
    if  len_s == 0:
      return 0
    if (len_s == 1):
      return 1
    char_dict = {}
    length_list = []
    substring_length = i = 0
    while i<len_s:
      for j in range(i,len_s):
        if s[j] not in char_dict.keys():
          char_dict[s[j]] = 1
          substring_length = substring_length+1
        else:
          length_list.append(substring_length)
          substring_length = 0
          char_dict = {}
          break
      i = i+1
    if length_list != []:
      return max(length_list)
    else:
      return 0