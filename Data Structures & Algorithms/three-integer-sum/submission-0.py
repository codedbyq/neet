class Solution:
    """
    nums = [-1,0,1,2,-1,-4]
               ^ ^       ^
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        for i,num in enumerate(sortedNums):
            j = i + 1
            k = len(sortedNums)-1
            while j < k:
                sum = num + sortedNums[j] + sortedNums[k]
                if sum == 0:
                    trips = [num, sortedNums[j], sortedNums[k]]
                    if trips not in res:
                        res.append(trips)
                if sum > 0:
                    k -= 1
                else:
                    j += 1
        return res