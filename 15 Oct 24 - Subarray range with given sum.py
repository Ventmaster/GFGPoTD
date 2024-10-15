# 15th October 2024
# Subarray range with given sum

class Solution:
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        d = {}
        curr_sum, count = 0, 0
        
        d[0] = 1
        
        for n in arr:
            curr_sum += n
            
            if (curr_sum - tar) in d:
                count += d[curr_sum - tar]
                
            if curr_sum in d:
                d[curr_sum] += 1
            else:
                d[curr_sum] = 1
                
        return count
