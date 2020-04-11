class Solution_split_string_balanced:
  def balancedStringSplit(self, s):
    len_s = len(s)
    r_count = l_count = 0
    balance_string_count = 0
    for i in range(0,len_s):
      if s[i] == 'R':
        r_count += 1
      else:
        l_count += 1
      if r_count == l_count:
        balance_string_count += 1
        r_count = l_count = 0
    return balance_string_count