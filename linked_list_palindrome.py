class Solution_isPalindrome:
  def isPalindrome(self, head: ListNode) -> bool:
    if head is None:
      return False
    if head.next is None:
      return True
    current = head
    rev_list_node = current
    while(current.next):
      temp = ListNode(current.next.val)
      temp.next = rev_list_node
      current = current.next
      rev_list_node = temp.next
    compare_head = head
    while(compare_head):
      if rev_list_node != compare_head:
        return False
      else:
        rev_list_node = rev_list_node.next
        compare_head = compare_head.next
    return True