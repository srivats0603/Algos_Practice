import copy
class Solution_permute_recursive_dup:
  def __init__(self):
    self.memo_permute = {}
  def compute_hk(self,list_permutations):
    hk = ''.join([str(num) for num in list_permutations]) 
    return hk
  def permuteUnique(self, nums):
    len_in_array = len(nums)
    if len_in_array <= 1:
      list_permutations = list(nums)
      hk = self.compute_hk(list_permutations)
      if hk not in self.memo_permute.keys():
        self.memo_permute[hk] = 1
        return [list_permutations]
      else:
        return []
    list_list_permutations = []
    first_num = nums[0]
    remain_permutations = self.permuteUnique(nums[1:len_in_array])
    print("permuting {} with remaining permutations {}".format(first_num,remain_permutations))
    for item in remain_permutations:
      len_item = len(item)
      for i in range(0,len_item+1):
        temp_item = copy.deepcopy(item)
        temp_item.insert(i,first_num)
        hk_temp = self.compute_hk(temp_item)
        
        if hk_temp not in self.memo_permute.keys():
          print("adding",temp_item)
          list_list_permutations.append(temp_item)
          self.memo_permute[hk_temp] = 1
          print("adding new hash key ",hk_temp)
        else:
          print("this hash key already present ->",hk_temp)
    return list_list_permutations