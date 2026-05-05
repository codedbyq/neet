class Solution:
    """
    one = 10
    two = 9
    nums = 0[2,9,8, 3, 6]
           0 2 9 10 12 16
                    
    """
    def rob(self, nums: List[int]) -> int:
        one,two = nums[0],0
        for i in range(1, len(nums)):
            temp = one
            one = max(two + nums[i], one)
            two = temp
        return one