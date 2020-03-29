class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution_oddEvenList:
  def oddEvenList(self, head: ListNode) -> ListNode:
    if (head is None) or (head.next is None):
      return head
    current_odd = ListNode(head.val)
    odd_head = current_odd
    current_even = ListNode(head.next.val)
    even_head = current_even
    current = head.next
    pos = 2 
    while(current.next):
      pos += 1
      if pos%2 == 0:
        current_even.next = ListNode(current.next.val)
        current_even = current_even.next
      else:
        current_odd.next = ListNode(current.next.val)
        current_odd = current_odd.next
      current = current.next
    current_odd.next = even_head
    return odd_head