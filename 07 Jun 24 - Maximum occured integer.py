# 07th June 2024
# Maximum occured integer

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        ##Your code here
        frequency = [0] * (maxx + 2)
        result = 0
        
        for i in range(n):
            frequency[l[i]] += 1
            
            if r[i] + 1 <= maxx:
                frequency[r[i] + 1] -= 1
                
        max_occur = freq[0]
        
        for i in range(1, maxx+1):
            frequency[i] += frequency[i-1]
            
            if frequency[i] > max_occur:
                max_occur = frequency[i]
                result = i
                
        return result
