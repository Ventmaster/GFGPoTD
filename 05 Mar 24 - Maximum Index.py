# 05 March 2024
# Maximum Index

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        ##Your code here
        if n == 1:
            return 0
            
        i, j = 0, n-1
        res = 0
        
        while i <= j:
            if a[i] <= a[j]:
                res = max(res, j-i)
                i = i + 1
                j = n - 1
            else:
                j = j - 1
        
        return res
