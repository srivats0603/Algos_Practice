class Solution_intersectionII:
  def intersection(self, nums1, nums2):
    len_1 = len(nums1)
    len_2 = len(nums2)
    num_dict = {}
    intersection_list = []
    if len_1 == 0 or len_2 == 0:
        return []
    for i in range(0,len_1):
      if nums1[i] not in num_dict.keys():
        num_dict[nums1[i]] = 1
      else:
        num_dict[nums1[i]] += 1
    for i in range(0,len_2):
      if (nums2[i] in num_dict.keys()) and (num_dict[nums2[i]] > 0):
        intersection_list.append(nums2[i])
        num_dict[nums2[i]] -= 1
    return intersection_list