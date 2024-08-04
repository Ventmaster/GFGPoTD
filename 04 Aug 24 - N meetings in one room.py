# 04th August 2024
# N meetings in one room

class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = sorted(zip(start, end), key = lambda x: x[1])
        count = 1
        last_end_time = meetings[0][1]
        
        for i in range(1, n):
            current_start_time, current_end_time = meetings[i]
        
            if current_start_time > last_end_time:
                count += 1
                last_end_time = current_end_time
                
        return count
