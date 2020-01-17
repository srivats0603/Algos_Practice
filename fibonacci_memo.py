class fibonnaci_memo():
  
  def __init__(self):
    self.memo = {}
  
  def compute_fibonacci(self,n):
    self.memo[1] = 0 
    self.memo[2] = self.memo[3] = 1
    if n in self.memo.keys():
      fib = self.memo[n]
    else:
      fib = self.compute_fibonacci(n-1)+self.compute_fibonacci(n-2)
      self.memo[n] = fib
    return fib


if __name__ == "__main__":
  import time
  fibonnaci_memo_obj = fibonnaci_memo()
  list_fib_memo = []
  start_time = time.time()
  for i in range(0,100):
    list_fib_memo.append(fibonnaci_memo_obj.compute_fibonacci(i+1))
  print("--- %s seconds ---" % (time.time() - start_time))
  #print(list_fib_memo)
