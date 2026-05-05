class Solution:
    """
    gas  = [1,2,3,4], 
    cost = [2,2,4,1]
    
     gas=[1,2,3]
    cost=[2,3,2]
              ^
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check sums
        if sum(gas) < sum(cost):
            return -1
        # setup variables
        n = len(gas)
        start = 0
        tank = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            tank += diff
            # not enough gas to get to next station
            if tank < 0:
                start = i + 1
                tank = 0
        return start