# 31st July 2024
# Longest Common Prefix of Strings

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        result = []
        M = min(arr, key = len)
        m, n = len(M), len(arr)
        
        if len(arr) == 1:
            return arr[0]
        
        for i in range(n - 1):
            c = ''
            
            for j in range(m):
                if arr[i][j] == arr[i+1][j]:
                    c += arr[i][j]
                else:
                    break
                
            if c != '':
                result.append(c)
                
        if len(result) >= n - 1:
            x = min(result, key = len)
            return x
        else:
            return -1
