import math
class Solution_sI:
  def __init__(self):
    pass
  def searchInsert(self, nums, target):
    len_nums = len(nums)
    if (len_nums == 0) or (target<=nums[0]):
      return 0
    if (target>nums[len_nums-1]):
      return len_nums
    l = 0
    h = len_nums-1
    while(l<=h):
      print("l={},h={},target={}".format(l,h,target))
      mid = math.floor((l+h)/2)
      if target == nums[mid]:
        return mid
      if target > nums[mid]:
        l = mid+1
      elif target < nums[mid]:
        h = mid-1
    if target > nums[l]:
      return l+1
    else:
      return l