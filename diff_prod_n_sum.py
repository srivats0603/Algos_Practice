class Solution_diff_prod_nd_sum:
  def subtractProductAndSum(self, n):
    sum_n = 0
    prod_n = 1
    if n<10:
      return 0
    while(n>0):
      this_digit = n%10
      sum_n += this_digit
      prod_n = prod_n*this_digit
      n = int(n/10)
    return prod_n-sum_n