# 27th September 2024
# K Sized Subarray Maximum

class Solution:
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        n = len(arr)
        li = []
        current_max = max(arr[:k])
        
        li.append(current_max)
        
        for i in range(1, n-k+1):
            if arr[i-1] == current_max:
                current_max = max(arr[i:i+k])
            else:
                current_max = max(current_max, arr[i+k-1])
                
            li.append(current_max)
            
        return li
