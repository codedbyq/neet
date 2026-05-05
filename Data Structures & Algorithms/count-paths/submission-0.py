class Solution:
    """
    1 2 3
    4 5 6
    7 8 9
                1
                ^
              2   4
              ^
            3   5
            ^   ^
          6.   6  8
          ^    ^  ^
         9.   9  9
    dp[m][n] = dp[m-1][n] + dp[m][n-1]
    """
    def uniquePaths(self, m: int, n: int) -> int:
        seen = [[0 for _ in range(n+1)] for _ in range(m+1)]
        def helper(m, n):
            if seen[m][n]:
                return seen[m][n]
            if m <= 1 or n <=1:
                seen[m][n] = 1
            else:
                seen[m][n] = helper(m-1,n) + helper(m,n-1)
            return seen[m][n]
        return helper(m,n)
        