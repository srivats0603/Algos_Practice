class Solution_unique_char:
  def firstUniqChar(self, s):
    len_s = len(s)
    if len_s == 0:
      return -1
    unique_char_dict = {}
    for i in range(0,len_s):
      if s[i] not in unique_char_dict.keys():
        unique_char_dict[s[i]] = 1
      else:
        unique_char_dict[s[i]] += 1
    for i in range(0,len_s):
      if unique_char_dict[s[i]] == 1:
        return i
    return -1