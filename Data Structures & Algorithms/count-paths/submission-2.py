class Solution:
    # 6 3 1
    # 3 2 1
    # x X X
     
    """
    brute force 2^(m*n) time and space
    if m or n == 1 return one
    unique paths is sum of paths going down and paths going right

    optimize using memoization O(m*n) time and space
    """
    # def uniquePaths(self, m: int, n: int) -> int:
    #     memo = [[0] * (n+1) for _ in range(m+1)]
    #     def helper(memo, m, n):
    #         if m == 1 or n == 1:
    #             return 1
    #         if memo[m][n]:
    #             return memo[m][n]
    #         memo[m][n] = helper(memo, m-1, n) + helper(memo, m, n-1)
    #         return memo[m][n]
    #     return helper(memo, m, n)

    """
    ideal optimization would be bottom up iterative solution
    where we only store the prev row so we can lower our space complexity
    X X X X X X
    X X X X X X 
    X X X X X X 
    """
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n
        for i in range(m-1, -1, -1):
            curr_row = [0] * n
            curr_row[n-1] = 1
            for j in range(n-2, -1, -1):
                curr_row[j] = curr_row[j+1] + prev_row[j]
            prev_row = curr_row
        return prev_row[0]
        