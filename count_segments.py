class Solution_countSegments:
  def isNonSpace(self,ch):
    if (ord(ch) != ord(' ')):
        return True
    else:
        return False

  def countSegments(self, s):
    len_s = len(s)
    valid_space_count = 0
    num_alphabets = 0
    if len_s == 0:
      return 0
    for i in range(0,len_s):
      if (s[i] == ' '):
        if (i != 0) and (i+1 != len_s) and (self.isNonSpace(s[i+1]) == True):
          valid_space_count += 1
          print("this i =",i)
          print("next character =",s[i+1])
      elif self.isNonSpace(s[i]) == True:
        num_alphabets += 1
    if (num_alphabets > 0):
      print(valid_space_count)
      if s[0] != ' ':
        return (valid_space_count+1)
      elif s[0] == ' ':
        return valid_space_count
    elif num_alphabets == 0:
      return 0