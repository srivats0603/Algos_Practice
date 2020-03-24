class Solution_reverseLinkedList:
  def reverseList(self, head):
    if head is None:
      return None
    current = head
    reversed_list_node = ListNode(current.val)
    current_rev = reversed_list_node
    while(current.next):
      temp = ListNode(current.next.val)
      temp.next = current_rev
      current = current.next
      current_rev = temp
    return current_rev