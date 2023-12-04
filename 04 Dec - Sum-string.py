# 04 December 2023
# Sum-string

class Solution:
    def isSumString (ob,S):
        # code here 
        n = len(S)
        
        def check(i, j, k):
            nonlocal S, n
            
            if k == n:
                return True
            
            if k > n:
                return False
                
            n1 = int(S[i:j])
            n2 = int(S[j:k])
            ns = str(n1+n2)
            
            if not S[k:].startswith(ns):
                return False
                
            return check(j, k, k+len(ns))
            
        for i in range(1, n):
            for j in range(i+1, n):
                if check(0, i, j):
                    return 1
        
        return 0 
