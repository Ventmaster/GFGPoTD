# 03rd June 2024
# Trail of ones

class Solution:
    def numberOfConsecutiveOnes(ob,n):
        # code here 
        modulo = 1e9 + 7
        prevprev, prev, result = 0, 1, 1
        
        for i in range(3, n + 1):
            add = (prevprev + prev) % modulo
            result = (2 * result + add) % modulo
            prevprev = prev
            prev = add
            
        return int(result)
