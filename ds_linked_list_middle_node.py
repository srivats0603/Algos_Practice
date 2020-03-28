class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

import math 

class Solution_middleNode:
  def count_elements(self,head):
    current = head
    count = 0
    while (current):
      count += 1
      current = current.next
    return count 
    
  def middleNode(self, head: ListNode) -> ListNode:
    count = self.count_elements(head)
    if count <= 1:
      return head
    mid = math.ceil((count+1)/2)
    current = head
    num_pass = 0
    while (current):
      num_pass += 1
      if (num_pass == mid):
        return current
      else:
        current = current.next