# 11 January 2024
# Remove K Digits

class Solution:

    def removeKdigits(self, S, K):
        # code here
        stack = []
        
        for digit in S:
            while K > 0 and stack and stack[-1] > digit:
                stack.pop()
                K -= 1
                
            stack.append(digit)
        
        while K > 0:
            stack.pop()
            K -= 1
        
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'
