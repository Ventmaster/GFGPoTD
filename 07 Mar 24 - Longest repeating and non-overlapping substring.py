# 07 March 2024
# Longest repeating and non-overlapping substring

class Solution:
    def longestSubstring(self, s , n):
        # code here 
        max_len = 0
        answer = "-1"
        
        i, j = 0, 0
        
        while i < n and j < n:
            sub = s[i:j+1]
            
            if s.find(sub, j+1) != -1:
                length = len(sub)
                
                if length > max_len:
                    answer = sub
                    max_len = length
            
            else:
                i += 1
            
            j += 1
            
        return answer
