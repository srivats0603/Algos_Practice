class Solution_sum_zero:
  def sumZero(self, n):
    if n == 1:
      return [0]
    return_list = []
    if n%2 == 0:
      for i in range(1,int(n/2)+1):
        return_list.append(-i)
        return_list.append(i)
    else:
      return_list.append(0)
      for i in range(1,int(n/2)+1):
        return_list.append(-i)
        return_list.append(i)
    return return_list