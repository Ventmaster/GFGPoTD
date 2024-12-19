# 19th December 2024
# Kth Missing Positive Number in a Sorted Array

class Solution:
    def kthMissing(self, arr, k):
        # code here
        curr = 1
        not_in = 0
        
        for i in range(len(arr)):
            while curr != arr[i]:
                curr += 1
                not_in += 1
                
                if not_in == k:
                    return curr-1
                    
            curr += 1
            
        return arr[len(arr)-1] + k - not_in
