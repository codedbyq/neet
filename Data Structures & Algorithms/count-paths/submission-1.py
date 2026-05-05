class Solution:
    # 2 1 0
    # 1 1 0
    # 0 0 0 
    """
    brute force 2^(m*n) time and space
    if m or n == 1 return one
    unique paths is sum of paths going down and paths going right
    """
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * (n+1) for _ in range(m+1)]
        def helper(memo, m, n):
            if m == 1 or n == 1:
                return 1
            if memo[m][n]:
                return memo[m][n]
            memo[m][n] = helper(memo, m-1, n) + helper(memo, m, n-1)
            return memo[m][n]
        return helper(memo, m, n)
        