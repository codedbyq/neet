"""
  c r a b t a
c 1 ? ? ? ? ? 
a ? ? 1 ? ? ? 
t ? ? ? ? 1 0

  a b c d
e ? ? ? ? 
f ? ? ? ? 
g ? ? ? ? 
h ? ? ? ? 

"""
class Solution:
    def helper(self, memo: List[List[int]], text1: str, text2: str, i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        if memo[i][j]:
            return memo[i][j]
        
        if text1[i] == text2[j]:
            memo[i][j] = 1 + self.helper(memo, text1, text2, i+1, j+1)
        else:
            memo[i][j] = max(self.helper(memo, text1, text2, i+1, j), self.helper(memo, text1, text2, i, j+1)) 
        return memo[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        memo = [[0] * M for _ in range(N)]
        return self.helper(memo, text1, text2, 0, 0)