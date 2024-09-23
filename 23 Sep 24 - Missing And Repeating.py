# 23rd September 2024
# Missing And Repeating

class Solution:
    def findTwoElement( self,arr): 
        # code here
        arr1 = []
        result = []
        seen = set()
        
        for i in range(len(arr)):
            arr1.append(i + 1)
            
        different = sorted(set(arr1) - set(arr))
        
        for i in arr:
            if i in seen:
                result.append(i)
                break
            
            seen.add(i)
            
        result.append(different[0])
        
        return result
