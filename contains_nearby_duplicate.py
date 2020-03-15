class Solution_near_dup:
  def containsNearbyDuplicate(self, nums, k):
    len_nums = len(nums)
    if len_nums <= 1:
      return False
    num_dict = {}
    for i in range(0,len_nums):
      if nums[i] in num_dict.keys():
        recent_distance = num_dict[nums[i]]-i
        if abs(recent_distance) <= k:
          #print(num_dict,recent_distance)
          return True
        else:
          num_dict[nums[i]] = i
      else:
        num_dict[nums[i]] = i
    #print(num_dict)
    return False