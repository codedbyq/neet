"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    inuition is a monotonic stack storing times in strictly increasing order
    intervals = [(5,8),(9,15)]
    intervals = [(0,30),(5,10),(15,20)]
    stack = 5,8
    """
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda it: it.start) # sort by start time
        for i in range(1, len(sorted_intervals)):
            curr, prev = sorted_intervals[i], sorted_intervals[i-1]
            if curr.start < prev.end:
                return False

        return True

                
