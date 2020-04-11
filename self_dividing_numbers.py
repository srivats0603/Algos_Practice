class Solution_selfDividingNumbers:
  def returnDigits(self,number):
    list_digits = []
    while(number>0):
      this_digit = (number%10)
      list_digits.append(this_digit)
      number = int(number/10)
    return list_digits
  
  def isDivisible(self,number):
    list_digits = self.returnDigits(number)
    if (0 in list_digits):
      return False
    for j in range(0,len(list_digits)):
      if (number%list_digits[j] != 0):
        return False
    return True
      
  def selfDividingNumbers(self, left, right):
    list_return = []
    for i in range(left,(right+1)):
      print("\n testing ",i)
      if i < 10:
        print("adding ",i)
        list_return.append(i)
      elif (i%10 != 0) and (self.isDivisible(i)):
        print("adding ",i)
        list_return.append(i)
    return list_return