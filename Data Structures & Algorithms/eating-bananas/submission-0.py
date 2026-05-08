import math
class Solution:
    """
    Input: piles = [1,4,3,2], h = 9
                    1 2 3 4
                    x + + +
    find max pile
    bin search from range 1 to max piles
    loop through piles to check how long it takes
    if koko can finish in h hours or less, try a smaller speed
    else current speed is too slow try a higher speed
    we can assume once our loop ends that left == right is the answer
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            total_speed = 0
            for pile in piles:
                total_speed += math.ceil(pile/mid)

            if total_speed <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
        