class solution_merge():
  def __init__(self):
    pass
  
  def merge(self,list_1,list_2):
    merged_list = []
    len_1 = len(list_1)
    len_2 = len(list_2)
    len_merged = len_1+len_2
    i = j = 0
    while ((i<len_1) and (j<len_2)):
      if list_1[i] < list_2[j]:
        merged_list.append(list_1[i])
        i = i+1
      else:
        merged_list.append(list_2[j])
        j = j+1
    for i_rem in range(i,len_1):
      merged_list.append(list_1[i_rem])
    for j_rem in range(j,len_2):
      merged_list.append(list_2[j_rem])
    return merged_list