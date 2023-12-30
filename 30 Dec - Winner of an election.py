# 29 December 2023
# Winner of an election

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d = {}
        
        for name in arr:
            if name in d.keys():
                d[name] += 1
            else:
                d[name] = 1
        
        li = []
        
        max1 = max(d.values())
        
        for key, value in d.items():
            if value == max1:
                li.append(key)
                
        li.sort()
        
        result = [li[0], str(max1)]

        return result
