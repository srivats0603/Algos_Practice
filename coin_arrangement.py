def arrangeCoins(self, n):
    if n == 0:
      return 0
    if n <= 2:
      return 1
    for i in range(1,n):
      if (i*(i+1)/2) == n:
        return i
      elif (i*(i+1)/2) > n:
        return i-1