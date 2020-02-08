class Solution_reverse_integer():
  def __init__(self):
    pass
  def get_rev_num(self,x):
    rev_num = 0
    while (x>0):
      rev_num = rev_num*10 + x%10
      x = x-x%10
      x = x/10
    return rev_num
  def reverse(self, x):
    if (x == 0):
      return 0
    if x<0:
      x = x*-1
      neg_multiplier = -1
    else:
      neg_multiplier = 1
    rev_num = self.get_rev_num(x)
    if rev_num> 2147483648:
      return 0
    else:
      return int(neg_multiplier*rev_num)