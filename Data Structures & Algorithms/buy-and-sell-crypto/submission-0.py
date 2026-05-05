class Solution:
    """
    max  = 6
    buy  = 0
    next = 1
    prices = [10,1,5,6,7,1]
                 ^ ^
    """
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            res = max(res, profit)
            if prices[left] > prices[right]:
                left = right
            right += 1

        return res