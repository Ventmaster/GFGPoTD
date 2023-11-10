# 10 November 2023
# Number following a pattern

class Solution:
    def printMinNumberForPattern(ob,S):
        result = []
        stack = []
        n = 1
        
        for char in S:
            stack.append(str(n))
            n = n + 1
            
            if char == "I":
                result = result + stack[::-1]
                stack = []
                
        stack.append(str(n))
        result = result + stack[::-1]
        
        return int(''.join(result))
