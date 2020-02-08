class Solution():
  def __init__(self):
    pass
  def twoSum(self, nums, target):
    len_nums = len(nums)
    if len_nums<2:
      return []
    two_sum_list = {}
    for i in range(0,len_nums):
      if (target-nums[i]) not in two_sum_list.keys():
        two_sum_list[nums[i]] = i
      else:
        return [i,two_sum_list[target-nums[i]]]