# 29th July 2024
# Row with max 1s

class Solution:
    def rowWithMax1s(self,arr):
        # code here
	n, m = len(arr), len(arr[0])
        result = 0
        row = -1 
        
        for i in range(n):
            curr = 0
            
            for j in range(m):
                if arr[i][j] == 1:
                    curr = m - j
                    
                    if curr > result or row == -1:
                        result, row = curr, i 
                    break
                
        return row
