# Passes test but takes too long
#class Solution:
#    def findErrorNums(self, nums: list[int]) -> list[int]:
#        for i in nums:
#            if nums.count(i) > 1:
#               duplicate = i
#        for i in range(1, len(nums) + 1):
#            if i not in nums:
#                missing = i
#                break
#        return duplicate, missing

# Works

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = sum(nums) - sum(set(nums))
        missing = (len(nums) * (len(nums) + 1) // 2) - sum(set(nums))
        return duplicate, missing