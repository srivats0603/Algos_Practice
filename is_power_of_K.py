class Solution_pow:
  def isPowerOfK(self,k,n):
    if n <= 0:
      return False
    if n == 1:
      return True
    while(n>1):
      if n%k != 0:
        return False
      else:
        n = n/k
    return True