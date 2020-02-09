class Solution:
  def __init__(self):
    pass
  
  def order_intervals(self,intervals):
    num_pairs = len(intervals)
    for i in range(0,num_pairs):
      intervals[i] = sorted(intervals[i])
    return intervals

  def sort_ordered_pairs(self,intervals):
    return sorted(intervals, key=lambda x: x[0])
  
  def compute_new_pointers_(self,intervals,left_pointer,right_pointer,right_element):
    if((right_element+1)<len(intervals)):
      next_right_pointer = intervals[right_element+1][1]
    else:
      next_right_pointer = -1
    for i in range((right_element+1),len(intervals)):
      if intervals[i][0]<=right_pointer:
        if intervals[i][1]>=right_pointer:
          right_pointer = intervals[i][1]
          right_element = i
          if((i+1)<len(intervals)):
            left_pointer = intervals[i+1][0]
            next_right_pointer = intervals[i+1][1]
        if intervals[i][1]<=right_pointer:
          right_element = i
          if((i+1)<len(intervals)):
            left_pointer = intervals[i+1][0]
            next_right_pointer = intervals[i+1][1]
      elif intervals[i][0] > right_pointer:
        left_pointer = intervals[i][0]
        next_right_pointer = intervals[i][1]
        right_element = i
        break
    
    return  left_pointer,right_pointer,right_element,next_right_pointer
  
  def merge(self,intervals):
    new_intervals = []
    if len(intervals) > 0:
      interval_elem_pos = 0
      num_pairs = len(intervals)
      #sort the list of lists
      intervals = self.order_intervals(intervals)
      intervals = self.sort_ordered_pairs(intervals)
      #print("sorted intervals",intervals)
      #left and right pointers initialized
      right_element = 0
      left_pointer = intervals[right_element][0]
      right_pointer = intervals[right_element][1]
      #find next pointers
      while (right_element<num_pairs):
        new_list_item = []
        new_list_item.append(left_pointer)
        left_pointer,right_pointer,right_element,next_right_pointer = self.compute_new_pointers_(intervals,left_pointer,right_pointer,right_element)
        new_list_item.append(right_pointer)
        if next_right_pointer>0:
          right_pointer = next_right_pointer
        new_intervals.append(new_list_item)
        #print("current new intervals list", new_intervals)
        if (new_list_item[1] >= intervals[num_pairs-1][1]): #terminate if right pointer is already pointing to the last element
          print("breaking because reached last element")
          break
        else:
          interval_elem_pos = interval_elem_pos+1
    return new_intervals