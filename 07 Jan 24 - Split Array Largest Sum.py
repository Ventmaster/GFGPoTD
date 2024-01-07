# 07 January 2024
# Split Array Largest Sum

class Solution:
    def func(self, arr, N, K, middle):
        # code here
        count = 1
        total_sum = 0
        
        for i in range(N):
            total_sum += arr[i]
            
            if total_sum > middle:
                count += 1
                total_sum = arr[i]
            
        return count <= K
        
    def splitArray(self, arr, N, K):
        l = max(arr)
        h = sum(arr)
        ans = -1 
        
        while l <= h:
            middle = l + (h-l)//2
            
            if self.func(arr, N, K, middle):
                ans = middle
                h = middle - 1
            else:
                l = middle + 1
        
        return ans
