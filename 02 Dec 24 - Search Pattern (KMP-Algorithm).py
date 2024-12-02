# 02nd December 2024
# Search Pattern (KMP-Algorithm)

class Solution:
    def search(self, pat, txt):
        # code here
        dp = [0] * len(pat)
        result = []
        
        for i in range(1, len(pat)):
            j = dp[i-1]
            
            while j > 0 and pat[j] != pat[i]:
                j = dp[j-1]
            
            dp[i] = j + int(pat[j] == pat[i])
            
        i, j = 0, 0
            
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                
                if j == len(pat):
                    result.append(i - j)
                    j = dp[j-1]
            
            else:
                if j > 0:
                    j = dp[j-1]
                else:
                    i += 1
                    
        return result
