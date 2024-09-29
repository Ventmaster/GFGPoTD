# 29th September 2024
# Total count

class Solution:
    def totalCount(self, k, arr):
        # code here
        count = 0
        
        for i in arr:
            if i <= k:
                count += 1
            else:
                count += (i // k)
                
                if i % k != 0:
                    count += 1
                    
        return count
