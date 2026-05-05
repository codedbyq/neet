class Solution:
    """
    brute force - time: O(n^3) space: O(1) 
    loop through i in range len(s)
    loop through j in range i,len(s)
    check isPalindrome(i,j) 
        if yes, counter += 1
        if no, break 
    return counter

    slightly optimized O(n^2) O(1)
    counter = 6
    s = "aaa"
            ^^
    loop through i in range len(s)
    setup our pointers for odd length palindromes (left, right) = i, i
    loop while in bounds of s: 0 <= pointer > len(s)
        if s[left] == s[right] we have a palindrome
            increment counter
            expand our pointers
        else
            break 
    repeat for even length palidromes so nested loop again
    check same parameters
    return counter
    """
    def countSubstrings(self, s: str) -> int:
        counter = 0
        # odd length palindromes
        for i in range(len(s)):
            left, right = i, i
            while 0 <= left and right < len(s):
                if s[left] != s[right]:
                    break
                counter += 1
                left -= 1
                right += 1
        # even length palindromes
        for i in range(len(s)):
            left, right = i, i+1
            while 0 <= left and right < len(s):
                if s[left] != s[right]:
                    break
                counter += 1
                left -= 1
                right += 1

        return counter
        