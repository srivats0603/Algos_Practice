class Solution_rmvDup:
  def __init__(self):
    pass
  def removeDuplicates(self,nums):
    nums += []
    if nums == []:
      return 0
    len_nums = len(nums)
    if len_nums == 1:
      return 1
    this_elem = nums[0]
    tota_non_dup_elem = 1
    i = 1
    while(i<len_nums):
      if nums[i] == this_elem:
        #print("removing ",nums[i])
        nums.pop(i)
        #print(nums)
        len_nums =  len_nums-1
      else:
        this_elem = nums[i]
        tota_non_dup_elem = tota_non_dup_elem+1
        #print("no element removed")
        #print(nums)
        i = i+1
    return tota_non_dup_elem#, nums