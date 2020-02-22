class Solution_plusOne:
  def plusOne(self, digits):
    new_array = []
    len_digits = len(digits)
    if len_digits == 0:
      return [1]
    if digits[-1] < 9:
      new_array = digits[0:-1]+[digits[-1]+1]
    else:
      new_array = self.plusOne(digits[0:-1])+[0]
    return new_array