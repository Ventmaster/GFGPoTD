# 29 February 2024
# Sum of bit differences

class Solution:
    def sumBitDifferences(self,arr, n):
        # code here
    	result = 0
    	
    	for i in range(32):
            setBits = 0
    	    unsetBits = 0
    	    
    	    for num in arr:
                if num & (1 << i):
    	            setBits += 1
    	        else:
    	            unsetBits += 1
    	            
            result = result + setBits * unsetBits * 2
    	    
    	return result
