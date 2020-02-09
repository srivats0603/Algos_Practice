class Solution_cnt_say_iter:
  def __init__(self):
    self.memo = {}
    self.memo[1] =  "1"
  def countAndSay(self, n):
    for j in range(2,n+1):
      last_num_string = self.memo[j-1]
      print("\n I am going to say the count and say the number ->",last_num_string)s
      len_nth = len(last_num_string)
      first_digit = last_num_string[0]
      self.memo[j] = ""
      this_digit_count = 1
      for i in range(1,len_nth):
        if last_num_string[i] == first_digit:
          this_digit_count = this_digit_count+1
        else:
          self.memo[j] = self.memo[j]+str(this_digit_count)+str(first_digit)
          first_digit = last_num_string[i]
          this_digit_count = 1
      self.memo[j] = self.memo[j]+str(this_digit_count)+str(first_digit) #explicitly for the last digit appearing in the string
    return self.memo[n]