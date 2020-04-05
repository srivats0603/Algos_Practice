class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution_insertion_sort_ll:
  def insertionSortList(self, head: ListNode) -> ListNode:
    if (head is None) or (head.next is None):
      return head
    sorted_head = ListNode(head.val)
    curr = head.next
    while(curr):
      print("inserting ",curr.val)
      curr_sorted = prev_sorted = sorted_head 
      while(curr_sorted):
        if (curr_sorted == sorted_head) and (curr.val < curr_sorted.val):
          print("list head {} replaced by {}".format(sorted_head.val,curr.val))
          sorted_head = ListNode(curr.val)
          sorted_head.next = curr_sorted
          prev_sorted = sorted_head
          curr_sorted = prev_sorted.next
          break
        elif (curr_sorted != sorted_head) and (curr.val < curr_sorted.val) and (curr.val >= prev_sorted.val):
          print("new node value {} inserted between {} and {}".format(curr.val,prev_sorted.val,curr_sorted.val))
          prev_sorted.next = ListNode(curr.val)
          prev_sorted.next.next = curr_sorted
          prev_sorted = prev_sorted.next
          curr_sorted = prev_sorted.next
          break
        elif (curr.val >= curr_sorted.val) and (curr_sorted.next == None):
          print("new node value {} inserted at the end, after {}".format(curr.val,curr_sorted.val))
          curr_sorted.next = ListNode(curr.val)
          prev_sorted = curr_sorted
          curr_sorted = prev_sorted.next
          break
        else:
          prev_sorted = curr_sorted
          curr_sorted = prev_sorted.next
      curr = curr.next
    return sorted_head