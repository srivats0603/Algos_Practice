class Solution_isIsomorphic:
  def isIsomorphic(self,pattern,str_x):
    len_pat = len(pattern)
    len_str_x = len(str_x)
    if len_pat != len_str_x:
      return False
    if (len_pat == 0) and (len_str_x == 0):
      return True
    pattern_dict = {pattern[0] : str_x[0]}
    letter_list = [str_x[0]]
    for i in range(1,len_pat):
      this_letter = str_x[i]
      if (pattern[i] not in pattern_dict.keys()):
        if this_letter not in letter_list:
          pattern_dict[pattern[i]] = this_letter
          letter_list.append(this_letter)
        else:
          #print(pattern_dict)
          return False
      elif (pattern_dict[pattern[i]] == this_letter):
        pass
      elif (pattern_dict[pattern[i]] != this_letter):
        #print(pattern_dict)
        return False
    #print(pattern_dict)
    return True