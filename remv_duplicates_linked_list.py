class Solution_remv_dups:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if (head is None) or (head.next is None):
      return head
    curr = head
    val_dict = {}
    while (curr):
      if curr.val not in val_dict.keys():
        val_dict[curr.val] = 1
      else:
        val_dict[curr.val] += 1
      curr = curr.next
    print(val_dict)
    curr = head
    prev = head
    while(curr):
      if val_dict[curr.val] > 1 :
        if curr == head:
          head = head.next
          curr = head
          prev = head
        else:
          prev.next = curr.next
          curr = curr.next
      else:
        prev = curr
        curr = curr.next
    return head