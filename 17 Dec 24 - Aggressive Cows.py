# 17th December 2024
# Aggressive Cows

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        left, right = 1, stalls[-1] - stalls[0]
        
        while left <= right:
            middle = left + (right-left) // 2
            prev, count = -10**8, 0
            
            for s in stalls:
                if s - prev >= middle:
                    count += 1
                    prev = s
                    
            if count >= k:
                left = middle + 1
            else:
                right = middle - 1
                
        return right
