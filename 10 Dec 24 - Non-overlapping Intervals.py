# 10th December 2024
# Non-overlapping Intervals

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals = sorted(intervals, key = lambda item: item[0])
        prev_end = intervals[0][1]
        result = 0
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            
            if prev_end > curr_start:
                result += 1
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end
                
        return result
