import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = string.ascii_lowercase + string.digits
        lowered = s.lower()
        left, right = 0, len(s)-1
        while left < right:
            if lowered[left] not in alpha:
                left += 1
                continue
            if lowered[right] not in alpha:
                right -=1 
                continue
            if lowered[left] != lowered[right]:
                return False
            left += 1
            right -= 1
        return True