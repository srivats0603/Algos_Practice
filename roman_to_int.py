class Solution_roman_to_int:
  def __init__(self):
    self.roman_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    self.subt_dict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
  def romanToInt(self, s):
    len_input_roman = len(s)
    out_sum = 0
    i = 0
    while i < len_input_roman:
      if ((i+1)<len_input_roman) and (s[i:i+2] in self.subt_dict):
        out_sum = out_sum+self.subt_dict[s[i:i+2]]
        i = i+2
      elif s[i] in self.roman_to_int:
        out_sum = out_sum+self.roman_to_int[s[i]]
        i = i+1
    return out_sum