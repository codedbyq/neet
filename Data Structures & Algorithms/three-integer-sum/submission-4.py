class Solution:
    """
    brute - 3 layer nested loop O(n^3) time O(1) space
    optimize by simplifying two layers to run in linear time
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        sortedNums = sorted(nums)
        for i, num in enumerate(sortedNums):
            left = i + 1
            right = len(sortedNums) - 1
            while left < right:
                currSum = num + sortedNums[left] + sortedNums[right]
                if currSum == 0:
                    trips = [num, sortedNums[left], sortedNums[right]]
                    if trips not in triplets:
                        triplets.append(trips)
                    
                if currSum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets
        