# 28th November 2024
# Implement Atoi

class Solution:
    def myAtoi(self, s):
        # Code here
        s = s.lstrip()
        sign = 1
        num = 0
        max_int = 2**31 - 1
        min_int = -2**31
        
        if s and s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
                
            s = s[1:]
            
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
            
        num = num * sign
        
        if num > max_int:
            return max_int
        elif num < min_int:
            return min_int
        else:
            return num
