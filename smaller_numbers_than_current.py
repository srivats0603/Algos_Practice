class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        len_nums = len(nums)
        elem_dict = {}
        j = 0
        for i in range(0,len_nums):
            #print(j,nums_sorted[i])
            if nums_sorted[i] not in elem_dict:
                elem_dict[nums_sorted[i]] = j
            j += 1
        #print(elem_dict)
        for i in range(0,len_nums):
            nums[i] = elem_dict[nums[i]]
        return nums