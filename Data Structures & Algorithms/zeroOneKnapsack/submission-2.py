class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[0] * (capacity + 1) for _ in range(len(profit)+1)]
        return self.helper(profit, weight, 0, capacity, memo)
    
    def helper(self, profit, weight, i, cap, memo):
        if i == len(profit):
            return 0
        if memo[i][cap]:
            return memo[i][cap]
        # skip case
        memo[i][cap] = self.helper(profit, weight, i+1, cap, memo)
        # include case
        new_cap = cap - weight[i]
        if new_cap >= 0:
            new_profit = profit[i] + self.helper(profit, weight, i+1, new_cap,memo)
            memo[i][cap] = max(memo[i][cap], new_profit)

        return memo[i][cap]