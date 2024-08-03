# 03rd August 2024
# The Celebrity Problem

class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        start, stop = 0, n - 1
        
        while start < stop:
            if mat[start][stop] == 1:
                start += 1
            else:
                stop -= 1
                
        for index in range(n):
            if index == stop:
                continue
            
            if mat[index][stop] != 1 or mat[stop][index] != 0:
                return -1
                
        return stop
