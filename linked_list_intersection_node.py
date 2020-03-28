class Solution_IntersectionNode:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if (headA is None) or (headB is None):
      return None
    currentA = headA
    currentB = headB
    ll_val_dict = {}
    while (currentA):
      if currentA not in ll_val_dict.keys():
        ll_val_dict[currentA] = currentA.next
      currentA = currentA.next
    while (currentB):
      if currentB not in ll_val_dict.keys():
        currentB = currentB.next
      else:
        if ll_val_dict[currentB] == currentB.next:
          return currentB
        else:
          currentB = currentB.next