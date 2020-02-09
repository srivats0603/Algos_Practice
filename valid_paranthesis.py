class Solution_valid_paranthesis():
  def __init__(self):
    self.left_paran_map = {'[':']','{':'}', '(':')'}
    self.right_paran_map = {']':'[','}':'{', ')':'('}
  
  def isValid(self, s):
    paran_stack = []
    len_in_string = len(s)
    if len_in_string == 0:
      return True
    for i in range(0,len_in_string):
      if s[i] in self.left_paran_map.keys():
        paran_stack.append(s[i])
      elif s[i] in self.right_paran_map.keys():
        if len(paran_stack)>0:
          if paran_stack[-1] == self.right_paran_map[s[i]]:
            paran_stack.pop()
          else:
            return False
        else:
          return False
      else:
        return False
    if  paran_stack == []:
      return True
    else:
      return False