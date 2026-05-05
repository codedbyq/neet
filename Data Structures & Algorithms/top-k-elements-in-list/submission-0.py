"""
brute force - nlogn where n is num of values
set up a hash to store nums and the num of their occurences
iterate through nums incrementing the hash
sort the dict by value
iterate through result in range of k
populate result array
return 
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        i (count) = 0 1 2 3 4 5 6
        values    =   3 2 1
        """
        counter = {}
        freq = [ [] for _ in range(len(nums) + 1) ] # empty list for every num in nums

        # populate counter
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # populate freq array
        for num, occurence in counter.items():
            freq[occurence].append(num)

        # get k most frequent
        result = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result