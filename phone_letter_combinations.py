class Solution_letterCombinations:
  def __init__(self):
    self.map_num_let = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
  def all_comb_two_str_lists(self,list1,list2):
    list_comb = []
    len_list_1 = len(list1)
    len_list_2 = len(list2)
    for i in range(0,len_list_1):
      for j in range(0,len_list_2):
        list_comb.append(str(list1[i]+list2[j]))
    return list_comb
  def letterCombinations(self, digits):
    dig_len = len(digits)
    if dig_len == 0:
      return []
    list_list_chars = []
    if digits[dig_len-1] in self.map_num_let.keys():
      list2 = self.map_num_let[digits[dig_len-1]]
    else:
      return []
    for i in range(dig_len-2,-1,-1):
      if digits[i] in self.map_num_let.keys():
        list1 = self.map_num_let[digits[i]]
        list2 = self.all_comb_two_str_lists(list1,list2)
      else:
        return []
    return list2