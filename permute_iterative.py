import copy
class Solution_permute_iterative:
  def permute(self, nums):
    len_in_array = len(nums)
    if len_in_array <= 1:
      return [list(nums)]
    #initializing with 2 variables
    list_list_permutations = [[nums[0],nums[1]],[nums[1],nums[0]]]
    for i in range(2,len_in_array):
      new_list_permutations = []
      for item in list_list_permutations:
        len_item = len(item)
        for j in range(0,len_item+1):
          temp_item = copy.deepcopy(item)
          temp_item.insert(j,nums[i])
          new_list_permutations.append(temp_item)
      list_list_permutations = new_list_permutations
    return list_list_permutations