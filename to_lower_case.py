class Solution_lc:
  def toLowerCase(self, str_x):
    len_str = len(str_x)
    if len_str == 0:
      return str_x
    for i in range (0,len_str):
      if (ord(str_x[i])>= ord('A')) and (ord(str_x[i]) <= ord('Z')):
        str_x =  str_x[0:i]+chr((ord('a')-ord('A'))+(ord(str_x[i])))+str_x[(i+1):len_str]
    return str_x