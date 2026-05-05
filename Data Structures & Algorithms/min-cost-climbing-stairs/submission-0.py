class Solution:
    """
    cost = [1,2,3,0]
            3 2 3 0
    cost = [1,2,1,2,1,1,1,0]
            4 5 3 3 2 1 1 0
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-2], cost[-1]
        for i in range(len(cost)-3,-1,-1):
            val = cost[i]
            temp = one
            one = val + min(one, two)
            two = temp
        return min(one, two)

