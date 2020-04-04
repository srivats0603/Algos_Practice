class Solution_partition_ll:
  def partition(self, head: ListNode, x: int) -> ListNode:
    if (head is None) or (head.next is None):
      return head
    curr = head
    lo_curr = None
    up_curr = None
    lo_head = None
    up_head = None
    while (curr):
      if (curr.val < x) and (lo_curr is None):
        lo_head = ListNode(curr.val)
        lo_curr = lo_head
      elif (curr.val < x) and (lo_curr is not None):
        lo_curr.next = ListNode(curr.val)
        lo_curr = lo_curr.next
      elif (curr.val >= x) and (up_curr is None):
        up_head = ListNode(curr.val)
        up_curr = up_head
      elif (curr.val >= x) and (up_curr is not None):
        up_curr.next =ListNode(curr.val)
        up_curr = up_curr.next
      curr = curr.next
    if lo_curr:
      lo_curr.next = up_head
    else:
      lo_head = up_head
    return lo_head