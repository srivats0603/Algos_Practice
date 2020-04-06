class Solution_custom_sort:
  def customSortString(self, S, T):
    len_s = len(S)
    len_t = len(T)
    if (len_s == 0) or (len_t == 0):
      return T
    t_dict = {}
    t_no_pattern = ""
    for i in range(0,len_t):
      if T[i] in S:
        if T[i] not in t_dict.keys():
          t_dict[T[i]] = T[i]
        else:
          t_dict[T[i]] += T[i]
      else:
        t_no_pattern += T[i]
    return_string = ""
    for i in range(0,len_s):
      if S[i] in t_dict.keys():
        return_string += t_dict[S[i]]
    return (return_string+t_no_pattern)