class Solution_insertion_sort():
  """sort in ascending order"""
  def __init__(self):
    pass
  
  def insertion_sort(self,list_input):
    list_to_be_sorted = copy.deepcopy(list_input)
    for i in range(1,len(list_to_be_sorted)):
      print("i=",i," element",list_to_be_sorted[i])
      element_to_be_checked = list_to_be_sorted[i]
      for j in range((i-1),-1,-1):
        print(" j=",j," element",list_to_be_sorted[j])
        if list_to_be_sorted[j] > element_to_be_checked:
          print("moving this element to right ->", list_to_be_sorted[j])
          list_to_be_sorted[j+1] = list_to_be_sorted[j]
        elif list_to_be_sorted[j] <= element_to_be_checked:
          list_to_be_sorted[j+1] = element_to_be_checked
          break
      if element_to_be_checked < list_to_be_sorted[0]:
        list_to_be_sorted[0] = element_to_be_checked
      print("sorted array in this step",list_to_be_sorted)
    return list_to_be_sorted