class Solution_revWords:
  def reverseWords(self, s):
    len_s = len(s)
    if len_s == 0:
      return ''
    rev_str = ''
    rev_str_temp = ''
    for i in range(0,len_s):
      if s[i] != ' ':
        rev_str_temp = s[i]+rev_str_temp
      elif (s[i] == ' '):
        if rev_str == '':
          rev_str = rev_str_temp
        else:
          rev_str = rev_str+' '+rev_str_temp
        rev_str_temp = ''
    if rev_str == '':
      rev_str = rev_str_temp
    else:
      rev_str = rev_str+' '+rev_str_temp
    return rev_str