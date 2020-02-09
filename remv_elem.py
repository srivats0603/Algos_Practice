class Solution_rmvElem:
  def __init__(self):
    pass
  def removeElement(self, nums, val):
    if nums == []:
      return 0
    len_nums = len(nums)
    if (len_nums == 1) and (nums[0] !=val):
      return 1
    i = 0
    while(i<len_nums):
      if nums[i] == val:
        len_nums = len_nums-1
        nums.pop(i)
      else:
        i = i+1
    return len(nums)