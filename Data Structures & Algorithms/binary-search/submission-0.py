class Solution:
    """
    nums = [-1,0,2,4,6,8], target = 4
             ^         ^
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1
        