class Solution_wordPattern:
  def find_num_words(self,str_x,len_str_x):
    num_words = 1
    space_list = []
    for i in range(0,len_str_x):
      if str_x[i] == ' ':
        space_list.append(i)
        num_words = num_words+1
    space_list.append(len_str_x+1)
    return num_words,space_list
  
  def wordPattern(self, pattern, str_x):
    len_pat = len(pattern)
    len_str_x = len(str_x)
    num_words,space_list = self.find_num_words(str_x,len_str_x)
    if len_pat != num_words:
      return False
    pattern_dict = {pattern[0] : str_x[0:space_list[0]]}
    word_list = [str_x[0:space_list[0]]]
    for i in range(1,len_pat):
      this_word = str_x[(space_list[i-1]+1):space_list[i]]
      if (pattern[i] not in pattern_dict.keys()):
        if this_word not in word_list:
          pattern_dict[pattern[i]] = this_word
          word_list.append(this_word)
        else:
          #print("the patterns for the word {} don't match".format(this_word))
          return False
      elif (pattern_dict[pattern[i]] == this_word):
        #print(pattern_dict[pattern[i]],"matches",this_word, "and")
        pass
      elif (pattern_dict[pattern[i]] != this_word):
        #print("the words for the pattern {} don't match".format(pattern[i]))
        return False
    #print(pattern_dict)
    return True