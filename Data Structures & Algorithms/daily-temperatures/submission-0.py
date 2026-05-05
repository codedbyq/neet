from collections import deque
class Solution:
    """
    stack = [1 ]
    res   = [ 1, 4, 1, 2, 1, 0, 0]
    temps = [30,38,30,36,35,40,28]
              0  1  2  3  4  5  6
                             ^
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)
        return result