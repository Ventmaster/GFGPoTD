# 01st September 2024
# Max sum path in two arrays

class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        i, j = 0, 0
        m, n = len(arr1), len(arr2)
        s1, s2, result = 0, 0, 0
        
        while i < m or j < n:
            if i == m:
                s2 += arr2[j]
                j += 1
                continue
            
            if j == n:
                s1 += arr1[i]
                i += 1
                continue
            
            if arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
                
            elif arr1[i] > arr2[j]:
                s2 += arr2[j]
                j += 1
                
            else:
                s1 += arr1[i]
                i += 1
                s2 += arr2[j]
                j += 1
                
                result += max(s1, s2)
                s1, s2 = 0, 0
        
        result += max(s1, s2)
        
        return result
