from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j<k:
                add = nums[i]+nums[j]+nums[k]
                if add==target:
                    return add
                elif abs(add-target)<abs(result-target):
                    result = add
                if add>target:
                    k-=1
                else:
                    j+=1
                
        return result
