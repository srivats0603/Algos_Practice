class Solution_hamming_dist:
  def decToBin(self,x:int)-> str:
    str_bin = ""
    while(x>0):
      str_bin = str(x%2)+str_bin
      x = int(x/2)
    return str_bin
  
  def hammingDistance(self, x: int, y: int) -> int:
    bin_x = self.decToBin(x)
    bin_y = self.decToBin(y)
    len_bin_x = len(bin_x)
    len_bin_y = len(bin_y)
    if len_bin_x < len_bin_y:
      bin_x = (len_bin_y-len_bin_x)*"0" + bin_x
      len_bin_x = len_bin_y
    elif len_bin_x > len_bin_y:
      bin_y = (len_bin_x-len_bin_y)*"0" + bin_y
      len_bin_y = len_bin_x
    elif bin_x == bin_y:
      print("x , y are {} , {}".format(bin_x,bin_y))
      return 0
    hamming_distance = 0
    print("x , y are {} , {}".format(bin_x,bin_y))
    for i in range(0,len_bin_x):
      if bin_x[i] != bin_y[i]:
        hamming_distance += 1
    return hamming_distance