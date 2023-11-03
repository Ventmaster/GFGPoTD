# 03 November 2023
# Pythagorean Triplet

class Solution:
    def checkTriplet(self,arr, n):
    # code here
    dict = {}
    	
    for i in range(n):
        number = arr[i] * arr[i]
        dict[number] = 1
    	    
    for i in range(n):
        value = arr[i] * arr[i]
    	    
        for j in range(i):
    	    n_value = arr[j] * arr[j]
    	        
    	    if (abs(n_value - value) in dict):
                return True
    	            
    return False
