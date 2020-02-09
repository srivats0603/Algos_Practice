class Solution:
  def __init__(self):
    self.str_to_num_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'-':-1,'+':1}
  def find_pos_first_valid_char(self,str_x,len_str):
    start_point = 0
    for i in range(0,len_str):
      if str_x[i] == ' ':
        start_point = start_point+1
      else:
        break
    return start_point
  def myAtoi(self, str_x):
    len_str = len(str_x)
    num_returned = 0
    multiplier = 1
    if len_str == 0:
      return num_returned
    start_point = self.find_pos_first_valid_char(str_x,len_str)
    if (start_point == len_str)or(str_x[start_point] not in self.str_to_num_dict.keys()):
      return num_returned
    elif (str_x[start_point] == '-') or (str_x[start_point] == '+'):
      multiplier = self.str_to_num_dict[str_x[start_point]]
      start_point = start_point+1
    for i in range(start_point,len_str):
      if (str_x[i] in self.str_to_num_dict.keys()) and (str_x[i] != '+') and (str_x[i] != '-'):
        num_returned = num_returned*10+self.str_to_num_dict[str_x[i]]
      else:
        break
    if num_returned >= pow(2,31):
      if multiplier == -1:
        num_returned = pow(2,31)
      else:
        num_returned = pow(2,31)-1
    return num_returned*multiplier