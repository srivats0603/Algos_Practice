class Solution_anagram_group:
  def __init__(self):
    self.anagram_grp_dict = {}
    self.anagram_grp_list = {}
    
  def generate_hash_key(self,str_item,len_str):
    hash_key = 0
    for i in range(0,len_str):
      hash_key = hash_key+ord(str_item[i])
    return (str(len_str)+"_"+str(hash_key))
  
  def new_anagram_dict(self,str_item,len_str):
    new_dict = {}
    for i in range(0,len_str):
      if str_item[i] not in new_dict.keys():
        new_dict[str_item[i]] = 1
      else:
        new_dict[str_item[i]] = new_dict[str_item[i]]+1
    return new_dict
  
  def test_valid_anagram(self,compare_dict,target,target_len):
    for i in range(0,target_len):
      if (target[i] in compare_dict.keys()) and (compare_dict[target[i]]>0):
        compare_dict[target[i]] = compare_dict[target[i]]-1
      else:
        return False
    if sum(compare_dict.values()) == 0:
      return True
    else:
      return False
    
  def groupAnagrams(self, strs):
    len_strs = len(strs)
    if len_strs == 0:
      return []
    len_first_str = len(strs[0])
    hk_0 = self.generate_hash_key(strs[0],len_first_str)
    dict_0 = self.new_anagram_dict(strs[0],len_first_str)
    self.anagram_grp_dict[hk_0] = {"grp_0": dict_0}
    self.anagram_grp_list[hk_0] = {"grp_0":[strs[0]]} 
    for i in range(1,len_strs):
      this_len = len(strs[i])
      this_hk = self.generate_hash_key(strs[i],this_len)
      this_dict = self.new_anagram_dict(strs[i],this_len)
      this_grp_key = "grp_"+str(i)
      if this_hk not in self.anagram_grp_dict:
        self.anagram_grp_dict[this_hk] = {this_grp_key:this_dict}
        self.anagram_grp_list[this_hk] = {this_grp_key:[strs[i]]} 
      else:
        key_group_found = False
        for group_num in self.anagram_grp_dict[this_hk].keys():
          copy_dict = self.anagram_grp_dict[this_hk][group_num].copy()
          is_valid = self.test_valid_anagram(copy_dict,strs[i],this_len)
          if is_valid == True:
            self.anagram_grp_list[this_hk][group_num].append(strs[i])
            key_group_found = True
        if key_group_found == False:
          self.anagram_grp_dict[this_hk][this_grp_key]= this_dict
          self.anagram_grp_list[this_hk][this_grp_key] = [strs[i]] 
    list_return = []
    for hk in self.anagram_grp_list.keys():
      for group_num in self.anagram_grp_list[hk].keys():
        list_return.append(self.anagram_grp_list[hk][group_num])
    return list_return