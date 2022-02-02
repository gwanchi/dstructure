"""
Given an interval newInterval and an array of intervals, create a function that inserts that newInterval in the array, and to merge if necessary. Note that the intervals in the array are non-overlapping, and are sorted according to their starting point.
"""
def insertInterval(intervals, newInterval):
    output = []
    i = 0
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        output.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    output.append(newInterval)
    while i < len(intervals):
        output.append(intervals[i])
        i += 1
    return output