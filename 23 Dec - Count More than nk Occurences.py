# 23 December 2023
# Count More than n/k Occurences

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        p = n // k
        c = 0
        d = {}
        
        for i in arr:
            d[i] = d.get(i,0) + 1 
            
        for i in d:
            if d[i] > p:
                c = c+ 1
        
        return c
