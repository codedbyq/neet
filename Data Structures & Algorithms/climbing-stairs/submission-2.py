class Solution:
    """

              []
            [][]
          [][][]
        [][][][]
    | [][][][][]
    1 1 2 3 5 8
    """
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1                # one: 8
        one,two = 1,1               # two: 5
        for num in range(2, n+1):   # num: 6 < 5+1
            temp = one
            one = one + two
            two = temp
        return one
        