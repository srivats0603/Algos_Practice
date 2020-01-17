class fibonnaci():
  
  def __init__(self):
    pass
  
  def compute_fibonacci(self,n):
    if n==1:
      fib = 0
    elif (n==2) or (n==3):
      fib = 1
    elif n>3:
      fib = self.compute_fibonacci(n-1)+self.compute_fibonacci(n-2)
    return fib



if __name__ == "__main__":
  import time
  fibonnaci_obj = fibonnaci()
  list_fib = []
  start_time = time.time()
  for i in range(0,25):
    list_fib.append(fibonnaci_obj.compute_fibonacci(i+1))
  print("--- %s seconds ---" % (time.time() - start_time))
  #print(list_fib)
