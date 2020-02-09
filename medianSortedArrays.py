class Solution_median_sorted_arrays():
  def __init__(self):
    pass
  
  def findMedianSortedArrays(self,list_1,list_2):
    merged_list = []
    
    len_1 = len(list_1)
    len_2 = len(list_2)
    len_merged = len_1+len_2
    i = j = 0
    if len_1 == 0:
      if len_2 % 2 == 0:
        return (float(list_2[int(len_2/2)])+float(list_2[int(len_2/2)-1]))/2
      else:
        return float(list_2[int((len_2+1)/2)-1])
    if len_2 == 0:
      if len_1 % 2 == 0:
        return (float(list_1[int(len_1/2)])+float(list_1[int(len_1/2)-1]))/2
      else:
        return float(list_1[int((len_1+1)/2)-1])
    while ((i<len_1) and (j<len_2)):
      if list_1[i] < list_2[j]:
        merged_list.append(list_1[i])
        i = i+1
        if len(merged_list) == (len_merged+1)/2:
          #print(merged_list)
          return float(merged_list[-1])
        elif len(merged_list) > (len_merged+1)/2:
          #print(merged_list)
          return (float(merged_list[-1])+float(merged_list[-2]))/2
      else:
        merged_list.append(list_2[j])
        j = j+1
        if len(merged_list) == (len_merged+1)/2:
          #print(merged_list)
          return float(merged_list[-1])
        elif len(merged_list) > (len_merged+1)/2:
          #print(merged_list)
          return (float(merged_list[-1])+float(merged_list[-2]))/2
    for i_rem in range(i,len_1):
      merged_list.append(list_1[i_rem])
      if len(merged_list) == (len_merged+1)/2:
        #print(merged_list)
        return float(merged_list[-1])
      elif len(merged_list) > (len_merged+1)/2:
        #print(merged_list)
        return (float(merged_list[-1])+float(merged_list[-2]))/2
    for j_rem in range(j,len_2):
      merged_list.append(list_2[j_rem])
      if len(merged_list) == (len_merged+1)/2:
        #print(merged_list)
        return float(merged_list[-1])
      elif len(merged_list) > (len_merged+1)/2:
        #print(merged_list)
        return (float(merged_list[-1])+float(merged_list[-2]))/2