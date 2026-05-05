class Solution:
    """
    brute force - O(n^3) where n in length of s. nested loop * n. constant space
    loop through string - i
    next loop again to generate substrings starting with i
    create a helper function isPalindrome that help determine is substring is valid
    if isPalindrome, compare the longest sub to current sub
    return longest 

    slightly optimized option - O(n^2) for nested loop
    loop through s
    expand in both directions checking for equality - if left and right pointer are equal they are palindrome
    if valid then compare length to longest
    we need to do this a second time to cover the edge case of even length palindromes
    return longest
    """
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest = [0,0]
        # odd length palindromes
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]: # valid palindrome
                    if (right - left) > longest[1] - longest[0]:
                        longest = [left, right]
                    left -= 1
                    right += 1
                else:
                    break
        # even length palindromes
        for i in range(len(s)):
            left, right = i, i+1
            while left >= 0 and right < len(s):
                if s[left] == s[right]: # valid palindrome
                    if right - left > longest[1] - longest[0]:
                        longest = [left, right]
                    left -= 1
                    right += 1
                else:
                    break

        return s[ longest[0] : longest[1]+1 ]