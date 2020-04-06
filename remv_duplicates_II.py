class Solution_at_most_twice:
  def removeDuplicates(self, nums):
    len_nums = len(nums)
    if len_nums <=2:
      return len_nums
    this_elem = nums[0]
    this_elem_count = i = 1
    while(i<len_nums):
      print("next element",nums[i])
      if nums[i] == this_elem:
        this_elem_count += 1
        if this_elem_count > 2:
          nums.pop(i)
          len_nums -= 1
        else:
          i += 1
        print("modified array",nums)
      else:
        this_elem = nums[i]
        this_elem_count = 1
        i += 1
    return len_nums