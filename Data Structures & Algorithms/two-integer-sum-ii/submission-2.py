class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers = [1,2,3,4], target = 3
                   ^ ^
        """
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right +1]
            
            if sum > target:
                right -= 1
            else:
                left += 1
        return []