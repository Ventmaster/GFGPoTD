# 18th September 24
# Parenthesis Checker

class Solution:
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []
        
        for i in x:
            if i == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                
        if not stack:
            return True
            
        return False
