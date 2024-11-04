# 04th November 2024
# Find All Triplets with Zero Sum

class Solution:
    def findTriplets(self, arr):
        # Your code here
        result = []
        d = dict()
        
        for index, item in enumerate(arr):
            d[item] = d.get(item, [])
            d[item].append(index)
            
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                Sum = arr[i] + arr[j]
                
                for k in d.get(-Sum, []):
                    if k > i and k > j:
                        result.append(sorted([i, j, k]))
                        
        return result
