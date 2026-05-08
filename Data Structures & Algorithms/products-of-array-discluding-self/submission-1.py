class Solution:
    """
    prefix = 8
    i      = 1
    nums = [1,2,4,6]
           [48,24,12,8]
    suffix = 48
    j      = 2
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        prefix_product = 1
        for i in range(len(nums)):
            result[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= suffix_product
            suffix_product *= nums[j]

        return result