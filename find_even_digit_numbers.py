class Solution_findNumbers:
    def num_digits(self,nums):
        num_dig = 0
        while(nums>0):
            nums = int(nums/10)
            num_dig += 1
        return num_dig
    
    def findNumbers(self, nums: List[int]) -> int:
        len_nums = len(nums)
        num_even = 0
        for i in range(0,len_nums):
            #test_metric = self.num_digits(nums[i])
            test_metric = len(str(nums[i]))  #this method is faster on an average, than calculating the num_digits using method above??
            if test_metric%2 == 0:
                num_even += 1    
        return num_even