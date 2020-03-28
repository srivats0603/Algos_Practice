class Solution_getDecimalValue:
  def binaryToDecimal(self,bin_str,str_len):
    if str_len <= 1:
      return int(bin_str)
    decimal_num = 0
    for i in range(str_len-1,-1,-1):
      decimal_num += int(bin_str[i])*pow(2,(str_len-i-1))
    return decimal_num
    
  def getDecimalValue(self, head: ListNode) -> int:
    current = head
    bin_str = ""
    str_len = 0
    while(current):
      bin_str += str(current.val)
      str_len += 1
      current = current.next
    return self.binaryToDecimal(bin_str,str_len)