class Solution_lol:
  def lengthOfLastWord(self, s):
    len_s = len(s)
    if len_s == 0:
      return 0
    len_last_word = 0
    found_first_char = False
    for i in range(len_s-1,-1,-1):
      if (s[i] == ' ') and (found_first_char == True):
        break
      elif (s[i] != ' ') and (found_first_char == False):
        len_last_word = len_last_word+1
        found_first_char = True
      elif (s[i] != ' ') and (found_first_char == True):
        len_last_word = len_last_word+1      
    return len_last_word