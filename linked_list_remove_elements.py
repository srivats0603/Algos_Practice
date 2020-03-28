class Solution_removeElements:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    if head is None:
      return head
    prev_node = None
    current = head
    while (current):
      if current.val == val:
        if prev_node == None:
          #print("removed the head node",head.val)
          head = head.next
        else:
          prev_node.next = current.next
      else:
        prev_node = current      
      current = current.next
    return head