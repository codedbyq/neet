class Solution:
    """
    Input: nums = [3,4,5,6,1,2], target = 1
    # regardless when we split our array one half is going to be sorted
    # setup pointers left,right
    # loop while left <= right inclusive for search
        # once we find midpoint one side is guarenteed to be sorted
        # return mid if target found
        # check if target is within sorted range
            # adjust the window accordingly
    # return -1
    nums=[4,5,6,7,0,1,2]
                  ^   ^
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right -left ) // 2 # overflow safe
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # left is sorted
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right is sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1