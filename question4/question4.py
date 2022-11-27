from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        whole_list = sorted(nums1 + nums2)
        print(whole_list)
        if len(whole_list) % 2 == 0:
            return (whole_list[(len(whole_list) + 1) // 2] + whole_list[(len(whole_list) - 1) // 2])/2
        else:
            return whole_list[len(whole_list)//2]
