class Solution_addDigits:
  def addDigits(self, num):
    if num < 10:
      return int(num)
    else:
      c = 1
      num_sum = 0
      while(num>0):
        num_sum += num%10
        num = int((num-num%10)/pow(10,c))
        print(num_sum,num)
      return self.addDigits(num_sum)