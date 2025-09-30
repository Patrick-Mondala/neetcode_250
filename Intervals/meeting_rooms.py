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


# Time Complexity: O(N * log(N)) where N is the length of intervals due to sorting the intervals list
# Space Complexity: O(1) due to using constant extra space
def canAttendMeetings(intervals: list[Interval]) -> bool:
    intervals.sort(key = lambda interval: interval.start)

    for i in range(1, len(intervals)):
        prev_end = intervals[i - 1].end
        cur_start = intervals[i].start

        if cur_start < prev_end:
            return False

    return True

# Test Cases
intervals = [(0,30),(5,10),(15,20)]
assert canAttendMeetings(intervals) == False

intervals = [(5,8),(9,15)]
assert canAttendMeetings(intervals) == True