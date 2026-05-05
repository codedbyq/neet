"""
longest = max(0,3)
seen = zxy
       012
s    = "zxyzxyz"
           ^
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, start_idx = 0, 0
        seen = {}
        for curr_idx, char in enumerate(s):
            if char in seen:
                start_idx = max(start_idx, seen[char]+1)
            longest = max(longest, (curr_idx - start_idx) + 1)
            seen[char] = curr_idx
        return longest