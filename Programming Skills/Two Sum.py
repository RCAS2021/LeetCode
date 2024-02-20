# Brute force
#class Solution:
#    def twoSum(self, nums: list[int], target: int) -> list[int]:
#        for i in range(0, len(nums)):
#            for j in range(0, len(nums)):
#                if (nums[i] + nums[j]) == target:
#                    if(i == j):
#                        continue
#                    else:
#                        return i, j

# Using dictionary
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ma = {}
        
        for i in range(len(nums)):
            ma[nums[i]] = i
        
        for key, value in ma.items():
            for i in range(len(nums)):
                if key + nums[i] == target and value != i:
                    return value, i   