class Solution_dup_list:
  def containsDuplicate(self, nums):
    len_nums = len(nums)
    if len_nums <= 1:
      return False
    num_dict = {}
    for i in range(0,len_nums):
      if nums[i] in num_dict.keys():
        return True
      else:
        num_dict[nums[i]] = 1
    return False
    """if len(num_dict.keys()) == len_nums:
      return False
    else:
      return True"""