class Solution:
    def helper(self, nums, start, end):
        one, two = 0, 0
        for i in range(start, end):
            temp = one
            one = max(one, nums[i] + two)
            two = temp
        return one
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        return max(self.helper(nums, 1, len(nums)), self.helper(nums, 0, len(nums)-1))