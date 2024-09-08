# 08th September 2024
# Minimum Jumps

class Solution:
    def minJumps(self, arr):
        current = 0
        maximum = 0
        count = 0
        
        for i in range(len(arr) - 1):
            maximum = max(maximum, i + arr[i])
            
            if current == i:
                if maximum == i:
                    return -1
                
                count += 1
                current = maximum
                
        return count
