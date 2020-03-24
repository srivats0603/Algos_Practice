class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
     
class Solution_merge_LL:
  def insert_tail(self,current_node,val):
    if current_node:
      current_node.next = ListNode(val)
      current_node = current_node.next
    else:
      current_node = ListNode(val)
    return current_node
  
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
      return l2
    if l2 is None:
      return l1
    current1 = l1
    current2 = l2
    #head comparison
    if current1.val <= current2.val:
      merged_l = ListNode(current1.val)
      current1 = current1.next
    else:
      merged_l = ListNode(current2.val)
      current2 = current2.next
    current_merged_l = merged_l  
    while (current1) and (current2):
      if current1.val <= current2.val:
        current_merged_l = self.insert_tail(current_merged_l,current1.val)
        current1 = current1.next
      else:
        current_merged_l = self.insert_tail(current_merged_l,current2.val)
        current2 = current2.next
    while(current1):
      current_merged_l = self.insert_tail(current_merged_l,current1.val)
      current1 = current1.next
    while(current2):
      current_merged_l = self.insert_tail(current_merged_l,current2.val)
      current2 = current2.next
    
    return merged_l