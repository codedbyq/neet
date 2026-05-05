from collections import deque
"""
str = "([{}])"
             ^
stk = 
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opens = "({["
        closed = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in opens:
                stack.append(char)
                continue
            elif char in closed:
                if not stack or closed[char] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
        