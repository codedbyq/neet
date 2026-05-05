class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # k= (index, sum), v= num ways
        def helper(index, curr_sum):
            if index == len(nums):
                return 1 if target == curr_sum else 0
            key = (index, curr_sum)
            if key in memo:
                return memo[key]

            memo[key] = helper(index+1, curr_sum+nums[index]) + helper(index+1, curr_sum-nums[index])
            return memo[key]
        return helper(0,0)