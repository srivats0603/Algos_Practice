class Solution_detectCycle:
  def detectCycle(self, head: ListNode) -> ListNode:
    if head is None:
      return None
    current = head
    pos = 0
    node_dict = {}
    while (current):
      if current not in node_dict.keys():
        node_dict[current] = pos
        current = current.next
        pos += 1
      else:
        return current
    pos = -1
    return None