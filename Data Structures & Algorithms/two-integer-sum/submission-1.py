class Solution:
    """
    nums = [3,4,5,6], target = 6
    
    iterate nums
    find diff (target - num)
    check if diff is in memory
    if so return, if not save 
    after loop we can assume no match was found so return empty list
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[num] = i
        return []
        