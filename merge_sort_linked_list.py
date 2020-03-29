#merge sort for linkedlist
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution_merge_sort_LL:
  def mergeSortedList(self, head1,head2):
    if (head1 is None):
      return head2
    if (head2 is None):
      return head1
    current1 = head1
    current2 = head2
    if current1.val < current2.val:
      merged_head = ListNode(current1.val)
      current1 = current1.next
    else:
      merged_head = ListNode(current2.val)
      current2 = current2.next
    merged_current = merged_head
    while (current1) and (current2):
      if current1.val < current2.val:
        merged_current.next = ListNode(current1.val)
        current1 = current1.next
      else:
        merged_current.next = ListNode(current2.val)
        current2 = current2.next
      merged_current = merged_current.next
    while (current1):
      merged_current.next = ListNode(current1.val)
      current1 = current1.next
      merged_current = merged_current.next
    while (current2):
      merged_current.next = ListNode(current2.val)
      current2 = current2.next
      merged_current = merged_current.next
    return merged_head
  
  def findMidpoint(self,head):
    current = head
    len_ll = 0
    while (current):
      len_ll +=1
      current = current.next
    return int(len_ll/2)
  
  def splitList(self,head,midpoint):
    current = head
    pos = 0
    new_list_head = None
    while (current):
      pos += 1
      if pos == midpoint:
        new_list_head = current.next
        current.next = None
      else:
        current = current.next
    return new_list_head
  
  def sortList(self, head: ListNode) -> ListNode:
    if (head is None) or (head.next is None):
      return head
    current = head
    midpoint = self.findMidpoint(current)
    new_list_head = self.splitList(current,midpoint)
    return self.mergeSortedList(self.sortList(current),self.sortList(new_list_head))