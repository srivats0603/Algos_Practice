class Solution_del_node:
  def __init__(self):
    self.head = ListNode(4)
    self.head.next = ListNode(5)
    self.head.next.next = ListNode(1)
    self.head.next.next.next = ListNode(9)
    
  def deleteNode(self, node):
    current = self.head
    prev_node = None
    while (current):
      if current.val == node:
        if prev_node is None:
          self.head = self.head.next
        else:
          prev_node.next = current.next
        break
      else:
        prev_node = current
        current = current.next
    return