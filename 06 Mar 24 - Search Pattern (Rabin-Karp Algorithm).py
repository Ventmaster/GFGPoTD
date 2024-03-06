# 06 March 2024
# Search Pattern (Rabin-Karp Algorithm)

class Solution:
    def search(self, pattern, text):
        # code here
        result = []
        m, n = len(text), len(pattern)
        
        if m < n:
            return False
            
        for i in range(m-n+1):
            if text[i:i+n] == pattern:
                result.append(i+1)
                
        return result
