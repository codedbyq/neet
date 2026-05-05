class Solution:
    def helper(self, text1, text2, i, j, memo):
        if i == len(text1) or j == len(text2):
            return 0
        if memo[i][j]:
            return memo[i][j]
        
        if text1[i] == text2[j]:
            memo[i][j] = 1 + self.helper(text1, text2, i+1, j+1, memo)
        else:
            memo[i][j] = max(self.helper(text1, text2, i+1, j, memo), self.helper(text1, text2, i, j+1, memo))

        return memo[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * len(text2) for _ in range(len(text1))]
        return self.helper(text1, text2, 0,0, memo)