class Solution_sqrt:
  def mySqrt(self, x):   
    if x <= 1:
      return x
    n = 2
    while(n*n <= x):
      if n*n == x:
        return n
      else: 
        n += 1
    return n-1