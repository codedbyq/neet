class Solution:
    """
    nums = [2,9, 8, 3, 6]
            2 9 10 12 16
    neighbor= 12
    next    = 10
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        neighbor, next_neighbor = nums[0], 0
        for i in range(1,len(nums)):
            temp = neighbor
            neighbor = max(neighbor, nums[i] + next_neighbor)
            next_neighbor = temp
        return neighbor
        