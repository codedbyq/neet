class Solution:
    """
    nums = 3[3,4,3] -> 3[3,4,3,3,4,3]
           3 3 
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        one, two = 0,0
        for num in nums:
            temp = one
            one = max(one, num+two)
            two = temp
        return one