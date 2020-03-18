class Solution_reverseString:
  def reverseString(self, s):
    len_s = len(s)
    if len_s <= 1:
      return s
    print("original ",s)
    if (len_s)%2 != 0:
      mid = int(len_s/2)
    else:
      mid = int((len_s+1)/2)
    for i in range(0,mid):
      temp = s[i]
      s[i] = s[len_s-1-i]
      s[len_s-1-i] = temp
    print("reversed ",s)
    return