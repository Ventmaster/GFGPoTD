# 28th August 2024
# Sorting Elements of an Array by Frequency

class Solution:
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        # code here 
        d = {}
        
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
                
        arr = []
        
        for k, v in d.items():
            arr.append([k, v])
            
        arr.sort()
        arr.sort(key = lambda x: x[1], reverse = True)
        
        result = []
        
        for k, v in arr:
            for i in range(v):
                result.append(k)
                
        return result
