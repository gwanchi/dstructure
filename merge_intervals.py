"""
Given an array of intervals, create a function that returns an array where overlapping intervals are merged.
"""
def mergeIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    for i in range(len(intervals)-1):
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i+1][0] = intervals[i][0]
            intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            intervals[i] = []
    output = []
    for interval in intervals:
        if len(interval) != 0:
            output.append(interval)
    return output