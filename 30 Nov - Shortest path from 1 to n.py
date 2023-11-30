# 30 November 2023
# Shortest path from 1 to n

class Solution:
    def minimumStep (self, n):
        #complete the function here
        cnt = 0
        
        while (n != 1):
            if n % 3 == 0:
                cnt = cnt + 1
                n = n // 3
            else:
                cnt = cnt + 1
                n = n - 1
        
        return cnt 
