class Solution:
    def helper(self, nums, target, index, sum):
        if index == len(nums):
            if sum == target:
                return 1
            else:
                return 0
        
        # add the current number to sum
        # subtract the current number from sum
        return self.helper(nums, target, index+1, sum+nums[index]) + self.helper(nums, target, index+1, sum-nums[index])

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, 0)