class solution_merge_sort():
  def merge_sorted_arrays(self,list_1,list_2):
    len_list_1 = len(list_1)
    len_list_2 = len(list_2)
    i = 0
    j = 0
    merged_list = []
    while ((i<len_list_1) and (j<len_list_2)):
      if list_1[i]<list_2[j]:
        merged_list.append(list_1[i])
        i = i+1
      else:
        merged_list.append(list_2[j])
        j = j+1
    for x in range(i,len_list_1):
      merged_list.append(list_1[x])
    for y in range(j,len_list_2):
      merged_list.append(list_2[y])
    return merged_list
  def merge_sort_recur(self,input_list):
    len_input_list = len(input_list)
    if len_input_list <= 1:
      return input_list
    mid = int(len_input_list/2)
    list_1 = input_list[0:mid]
    list_2 = input_list[mid:len_input_list]
    return self.merge_sorted_arrays(self.merge_sort_recur(list_1),self.merge_sort_recur(list_2))