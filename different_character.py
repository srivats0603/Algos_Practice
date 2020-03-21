class Solution_diff_char:
  def findTheDifference(self, s, t):
    len_s = len(s)
    len_t = len_s+1
    char_dict = {}
    if len_s == 0:
      return t
    for i in range(0,len_s):
      if s[i] not in char_dict.keys():
        char_dict[s[i]] = 1
      else:
        char_dict[s[i]] += 1
    for i in range(0,len_t):
      if (t[i] not in char_dict.keys()) or (char_dict[t[i]] == 0):
        return t[i]
      else:
        char_dict[t[i]] -= 1
    retu