class Solution_mult_str:
  def __init__(self):
    self.str_to_num_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    
  def multiply(self, num1, num2):
    num1_len = len(num1)
    num2_len = len(num2)
    c1 = 1
    c2 = 1
    num1_int = 0
    num2_int = 0
    for i in range(num1_len-1,-1,-1):
      num1_int = num1_int+c1*(self.str_to_num_dict[num1[i]])
      c1 = c1*10
    for j in range(num2_len-1,-1,-1):
      num2_int = num2_int+c2*(self.str_to_num_dict[num2[j]])
      c2 = c2*10
    print(num1_int,num2_int,num1_int*num2_int)
    return str(num1_int*num2_int)