class Solution_createTargetArray:
    def insert(self,target,i,n,len_target):
        target = target[0:i]+[n]+target[i:len_target]
        return target
    
    def createTargetArray(self, nums, index):
        len_nums = len(nums)
        target = []
        len_target = 0
        for i in range(0,len_nums):
            len_target += 1
            #target.insert(index[i],nums[i])
            target = self.insert(target,index[i],nums[i],len_target)
        return target