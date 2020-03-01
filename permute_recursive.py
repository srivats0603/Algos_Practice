import copy
class Solution_permute_recursive:
  def permute(self, nums):
    print("permuting ",nums)
    len_in_array = len(nums)
    if len_in_array <= 1:
      return [list(nums)]
    list_list_permutations = []
    first_num = nums[0]
    remain_permutations = self.permute(nums[1:len_in_array])
    if len(remain_permutations) == 1:
      return [[first_num,remain_permutations[0][0]],[remain_permutations[0][0],first_num]]
    for item in remain_permutations:
      len_item = len(item)
      for i in range(0,len_item+1):
        temp_item = copy.deepcopy(item)
        temp_item.insert(i,first_num)
        list_list_permutations.append(temp_item)
    return list_list_permutations