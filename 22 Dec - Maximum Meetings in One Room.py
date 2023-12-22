# 22 December 2023
# Maximum Meetings in One Room

from typing import List


class Solution:
    def maxMeetings(self, n : int, s : List[int], f : List[int]) -> List[int]:
        # code here
        temp = sorted([[s[i], f[i], i+1] for i in range(n)], key = lambda j: (j[1], j[2]))
        result = [temp[0][2]]
        
        for i in temp[1:]:
            if i[0] > f[result[-1]-1]:
                result.append(i[2])
                
        return sorted(result)
