class Solution_perfect_square:
  def isPerfectSquare(self, num):
    if num <= 1:
      return True
    n = 2
    while(n*n <= num):
      if n*n == num:
        return True
      else: 
        n += 1
    return False