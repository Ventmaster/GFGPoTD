# 18th December 2024
# Allocate Minimum Pages

class Solution:
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n = len(arr)
        low, high = max(arr), sum(arr)
        
        if n < k:
            return -1
            
        while low < high:
            middle = (low + high) // 2
            
            if Solution.func(arr, k, middle):
                high = middle
            else:
                low = middle + 1
                
        return low
        
            
    def func(arr, k, maxPages):
        students = 1
        curr_sum = 0
            
        for pages in arr:
            if curr_sum + pages > maxPages:
                students += 1
                curr_sum = pages
                    
                if students > k:
                    return False
            else:
                curr_sum += pages
                    
        return True
