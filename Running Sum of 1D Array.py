class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        
        for i in range(0, len(nums)):
            result[i] = result[i-1] + nums[i]
        return result