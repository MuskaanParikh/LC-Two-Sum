from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums and i is not nums.index(complement):
            return [nums.index(complement), i]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))