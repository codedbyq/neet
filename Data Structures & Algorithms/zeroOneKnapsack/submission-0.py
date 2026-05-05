class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.helper(profit, weight, 0, capacity)
    
    def helper(self, profit, weight, i, cap):
        if i == len(profit):
            return 0
        # skip case
        max_profit = self.helper(profit, weight, i+1, cap)
        # include case
        new_cap = cap - weight[i]
        if new_cap >= 0:
            new_profit = profit[i] + self.helper(profit, weight, i+1, new_cap)
            max_profit = max(max_profit, new_profit)

        return max_profit