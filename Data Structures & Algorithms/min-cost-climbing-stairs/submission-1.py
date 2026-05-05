class Solution:
    """
    cost = [1,2,1,2,1,1,1]
            ^
    one  = 4
    two  = 5
                
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        elif len(cost) == 0:
            return 0
        one, two = cost[-2], cost[-1]
        for i in range(len(cost)-3, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp
        return min(one, two)