# 10th October 2024
# Max distance between same elements

class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        d = {}
        
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] = [d[arr[i]][0], i]
            else:
                d[arr[i]] = [i, 0]
                
        result = 0
        
        for key, value in d.items():
            result = max(value[1] - value[0], result)
            
        return result
