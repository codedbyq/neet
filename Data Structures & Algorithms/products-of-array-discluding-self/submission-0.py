"""
    nums = [1,2,4,6]
            1 1 2 8
          48 24 6 1
         48 24 12 8
12
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # first find all the products that come before nums[i]
        prefix_product = 1
        for index in range(len(nums)):
            result[index] = prefix_product
            prefix_product *= nums[index]

        # then multiply by all the products that come after nums[i]
        suffix_product = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] *= suffix_product
            suffix_product *= nums[index]

        return result