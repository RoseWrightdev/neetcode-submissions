class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        stk = [intervals[0]]

        for start, end in intervals:
            top_end = stk[-1][1]
            if top_end >= start:
                stk[-1][1] = max(end, top_end)
            else:
                stk.append([start, end])
        return stk