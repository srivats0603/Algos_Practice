#3. Linked Lists
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None  # initialize head to None
  def is_empty(self):
    if self.head is None:
      return True
    else:
      return False
  def insert_head(self,head):
    new_head = ListNode(head)
    if self.head:
      new_head.next = self.head
    self.head = new_head
  def insert_tail(self,tail):
    new_tail = ListNode(tail)
    if self.head is None:
      self.insert_head(new_tail)
    else:
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_tail
  def print_list(self):
    if self.head is None:
      print(None)
    else:
      current = self.head
      while(current):
        print(current.val)
        current = current.next
  def delete_head(self):
    current = self.head
    if self.head:
      self.head = self.head.next
      current.next = None
    return current
  def delete_tail(self):
    current = self.head
    if current.next is None:
      self.delete_head()
    if current.next.next: #going upto second last element
      current = current.next
    temp = current.next
    current.next = None
    return temp
    
if __name__ == "__main__":
  #list 1 : 1->2->4
  #list 2:  1->3->4
  list1 = LinkedList()
  list1.insert_head(1)
  list1.insert_tail(2)
  list1.insert_tail(4)
  print("list1")
  list1.print_list()
  list2 = LinkedList()
  list2.insert_head(1)
  list2.insert_tail(3)
  list2.insert_tail(4)
  print("list2")
  list2.print_list()