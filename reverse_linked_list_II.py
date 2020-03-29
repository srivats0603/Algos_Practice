class Solution_reverse_LL_II:
  def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if (m >= n) or (head is None) or (head.next is None):
      return head
    current = head
    l1_head = current
    curr_pos = 0
    l1_tail = None
    l2_head = None
    l2_tail = None
    l3_head = None
    while(current):
      curr_pos += 1
      if curr_pos == m-1:
        l1_tail = current
      elif curr_pos == m:
        l2_head = current
      elif curr_pos == n:
        l2_tail = current
        if (current.next):
          l3_head = current.next
      current = current.next
    rev_l2_tail = ListNode(l2_head.val)
    if (l2_tail):
      l2_tail.next = None
    prev_rev = rev_l2_tail
    current_rev = l2_head.next
    while (current_rev):
      temp = ListNode(current_rev.val)
      temp.next = prev_rev
      current_rev = current_rev.next
      prev_rev = temp
    if l1_tail:
      l1_tail.next = prev_rev
    else:
      l1_tail = l1_head = prev_rev
    if l3_head:
      rev_l2_tail.next = l3_head
    return l1_head