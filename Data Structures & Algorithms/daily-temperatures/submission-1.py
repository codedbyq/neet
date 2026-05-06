from collections import deque
class Solution:
    """
    stack        = [5,6]
    temperatures = [30,38,30,36,35,40,28]
    result       = [ 1, 4, 1, 2, 1, 0, 0]

    create a monotonic stack to store temps in DECREASING order
    create result array, 0 for every index same length as temps
    iterate through temps
    check if temps[i] is less than or equal to top of stack
        if yes, add index to stack
        if no, we have found our next warmer day for top of the stack
            we can iterate through the stack while still temps[i] is less than or equal to top of stack, 
            popping the top and updating position in result array
            lastly add curr temp to stack
    return result
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = deque() # store in strictly DECREASING order

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pos = stack.pop()
                days_since = i - pos
                result[pos] = days_since
            stack.append(i)

        return result