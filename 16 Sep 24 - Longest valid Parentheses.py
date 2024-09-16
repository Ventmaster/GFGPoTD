# 16th September 2024
# Longest valid Parentheses

class Solution:
    def maxLength(self, str):
        # code here
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(str):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
                    
        return max_len
