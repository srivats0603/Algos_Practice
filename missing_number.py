class Solution_missingNumber:
  def missingNumber(self, nums):
    n = len(nums)
    sum_n = n*(n+1)/2
    sum_arr = sum(nums)
    return int(sum_n-sum_arr)