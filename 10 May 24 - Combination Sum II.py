# 10 May 2024
# Combination Sum II

class Solution:
    def CombinationSum2(self, arr, n, k):
        # code here
        arr.sort()
        result = []
        
        def dfs(index, sum1, path, result):
            if sum1 == k:
                result.append(path)
                
            if sum1 > k:
                return
            
            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i-1]:
                    continue
                
                dfs(i+1, sum1 + arr[i], path + [arr[i]], result)
                
        dfs(0, 0, [], result)
        
        return result
