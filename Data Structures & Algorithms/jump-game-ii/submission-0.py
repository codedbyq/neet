class Solution:
    """
    memo = {5:0,4:1,3:2,2:3,1:1,0}
    nums = [2,4,1,1,1,1]
              ^
    """
    def jump(self, nums: List[int]) -> int:
        # setup window pointers
        left = right = 0
        # setup return variable
        min_jumps = 0                                           #jumps=2
        # loop while right pointer is less than len(nums)
        while right < len(nums) - 1:                                # left=3, right=5        
            biggest_jump = 0                                    # biggest=2
            # iterate our window and find the biggest jump
            for i in range(left, right + 1):
                biggest_jump = max(biggest_jump, i + nums[i])
            # update our new window range
            left = right + 1
            right = biggest_jump
            # increment min_jumps
            min_jumps += 1
        # exit loop and return result
        return min_jumps
