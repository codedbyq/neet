class Solution:
    """
    4 = 2+2,2+1+1,1+1+1+1,1+1+2+2,1+2+2
    3 = 2+1,1+1+1,1+2
    2 = 2+0, 1+1
    1 = 1+0
    0 = 1
    """
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n < 2:
                memo[n] = 1
            else:
                memo[n] = helper(n-1) + helper(n-2)
            return memo[n]

        return helper(n)