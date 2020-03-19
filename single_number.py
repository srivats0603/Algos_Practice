class Solution_singleNumber:
  def singleNumberII(self,nums):
    len_nums = len(nums)
    sum_nums_expected = 0
    num_dict = {}
    sum_nums_available = 0
    for i in range(0,len_nums):
      sum_nums_available += nums[i]
      if nums[i] not in num_dict.keys():
        num_dict[nums[i]] = 1
        sum_nums_expected += nums[i]
    return (2*sum_nums_expected-sum_nums_available)
  def singleNumber(self, nums):
    len_nums = len(nums)
    num_dict = {}
    for i in range(0,len_nums):
      if nums[i] not in num_dict.keys():
        num_dict[nums[i]] = 1
      else:
        num_dict[nums[i]] += 1
    for key,value in num_dict.items():
      if value == 1:
        return key