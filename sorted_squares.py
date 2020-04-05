class Solution_sorted_squares:
  def rev_list(self,list_i,len_list):
    list_1 = [0]*len_list
    for j in range(len_list-1,-1,-1):
        list_1[len_list-1-j] = (list_i[j])
    return list_1
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
  def sortedSquares(self, A):
    len_A = len(A)
    if len_A == 0:
      return A
    elif len_A == 1:
      return [A[0]*A[0]]
    sep_point = -1
    square_list = [0]*len_A
    for i in range(0,len_A):
      if (A[i] >=0) and (sep_point == -1):
        sep_point = i
      square_list[i] = (A[i]*A[i])
    if sep_point == -1:
      list_1 = self.rev_list(square_list,len_A)
      return list_1
    elif sep_point == 0:
      return square_list
    else:
      list_1 = self.rev_list(square_list[0:sep_point],sep_point)
      return self.merge_sorted_arrays(list_1,square_list[sep_point:len_A])