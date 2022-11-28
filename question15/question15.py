from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i>0 and nums[i-1] == nums[i]:
            continue
        j = i+i
        k = len(nums)-1
        while j<k:
            target = nums[i] + nums[j] + nums[k]
            if target>0:
                k -= 1
            elif target<0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j-1]==nums[j] and j<k:
                    j += 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))