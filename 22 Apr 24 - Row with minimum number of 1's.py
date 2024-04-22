# 22 April 2024
# Row with minimum number of 1's

class Solution:
    def minRow(self,n,m,a):
        #code here
        b = []
        
        for row in a:
            b.append(sum(row))
        
        return b.index(min(b)) + 1
