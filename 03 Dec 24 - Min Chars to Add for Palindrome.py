# 03rd December 2024
# Min Chars to Add for Palindrome

class Solution:
    def minChar(self, s):
        #Write your code here
        s_reverse = s[::-1]
        temp = s + '#' + s_reverse
        
        lps = [0] * len(temp)
        j = 0 
        
        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j-1]
                
            if temp[i] == temp[j]:
                j += 1
                
            lps[i] = j
            
        return len(s) - lps[-1]
