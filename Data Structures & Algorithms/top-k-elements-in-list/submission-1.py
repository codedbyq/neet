import heapq

class Solution:
    """
    nums = [1,2,2,3,3,3], k = 2
    freq = { 1:1, 2:2, 3:3 }
    
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        res = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            res.append(num)

        return res
        

        