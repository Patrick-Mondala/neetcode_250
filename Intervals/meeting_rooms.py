'''
Meeting Rooms
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def canAttendMeetings(intervals: list[Interval]) -> bool:
    """
    Implement canAttendMeetings
    """

# Test Cases
intervals = [(0,30),(5,10),(15,20)]
assert canAttendMeetings(intervals) == False

intervals = [(5,8),(9,15)]
assert canAttendMeetings(intervals) == True