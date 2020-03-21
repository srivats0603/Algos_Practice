class Solution_freq_sort:
  def frequencySort(self, s):
    len_s = len(s)
    if len_s <=2:
      return s
    char_dict = {}
    for i in range(0,len_s):
      if s[i] not in char_dict.keys():
        char_dict[s[i]] = 1
      else:
        char_dict[s[i]] += 1
    char_tup_list = [v*k for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse =True)]
    new_s = ''.join(str(elem) for elem in char_tup_list)
    return new_s