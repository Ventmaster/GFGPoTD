# 26 March 2024
# Additive sequence

class Solution:
    def isAdditiveSequence(self, n):
        #code here
        if len(n) < 3:
            return 0
            
        def is_valid_number(s):
            return len(s) == 1 or s[0] != '0'
            
        for i in range(1, len(n)-1):
            if not is_valid_number(n[:i]):
                continue
            
            for j in range(i+1, len(n)):
                if not is_valid_number(n[i:j]):
                    continue
                
                n1 = int(n[:i])
                n2 = int(n[i:j])
                
                k = j
                
                while k < len(n):
                    n3 = n1 + n2
                    str_n3 = str(n3)
                    
                    if not n.startswith(str_n3, k):
                        break
                    
                    k += len(str_n3)
                    
                    n1, n2 = n2, n3
                    
                    if k == len(n):
                        return 1
                        
        return 0
