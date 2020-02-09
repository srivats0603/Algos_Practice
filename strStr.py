class Solution_strStr:
  def __init__(self):
    pass
  def strStr(self, haystack, needle):
    if needle == "":
      return 0
    return_position = -1
    needle_length = len(needle)
    haystack_length = len(haystack)
    for i in range(0,haystack_length):
      matched_chars = 0
      if haystack[i] == needle[0]:
        matched_chars = matched_chars+1
        print("matched ",needle[0])
        if (haystack_length-i-1) >= (needle_length-1):
          for j in range(1,needle_length):
            if haystack[i+j] == needle[j]:
              matched_chars = matched_chars+1
              print("matched ",needle[j])
            else:
              break
          if matched_chars == (needle_length):
            return_position = i
            break
        else:
          return -1
    return return_position