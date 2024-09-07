# 07th September 2024
# Nth Natural Number

def func(n):
    if n < 9:
        return n
        
    return 10 * func(n//9) + n%9

class Solution:
    def findNth(self,n):
        #code here
        return func(n)
