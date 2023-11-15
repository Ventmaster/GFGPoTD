# 15 November 2023
# Better String 

class Solution:
    def betterString(self, str1, str2):
        def distinctsubsequence(s):
            n = len(s)
            
            dp = [0] * (n+1)
            dp[0] = 1
            
            map = {}
            
            for i in range(1, n+1):
                dp[i] = 2 * dp[i-1]
                
                ch = s[i-1]
                
                if ch in map:
                    j = map[ch]
                    
                    dp[i] = dp[i] - dp[j-1]
                    
                map[ch]=i
                
            return dp[n]
            
        if distinctsubsequence(str1)>=distinctsubsequence(str2):
            return str1
        else:
            return str2
