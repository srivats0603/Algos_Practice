class Solution_palin_num:
  def __init__(self):
    pass
  def isPalindrome(self, x):
    x_orig = x
    if x_orig < 0:
      return False
    reverse_x = 0
    while x>0:
      print('\n',reverse_x,x,10)
      reverse_x = reverse_x*10+x%10
      x = int(x/10)
    if x_orig == reverse_x:
      return True
    else:
      return False