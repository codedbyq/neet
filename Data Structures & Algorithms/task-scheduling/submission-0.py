from collections import deque
import heapq 

class Solution:
    """
    tasks = ["X","X","Y","Y"], n = 2 => 5
    # setup frequency counter using dict
    # setup queue to track tasks in cooldown
    # use a max heap to get tasks
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequency of each task - O(n) time and space
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        # setup max heap - O(n) time and space
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        cycles = 0
        cooldown = deque() # pair of [-count, wait_time]
        while max_heap or cooldown:
            cycles += 1

            if not max_heap:
                cycles = cooldown[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count: 
                    cooldown.append([count, cycles + n])
            if cooldown and cooldown[0][1] == cycles:
                heapq.heappush(max_heap, cooldown.popleft()[0])
    
        return cycles
