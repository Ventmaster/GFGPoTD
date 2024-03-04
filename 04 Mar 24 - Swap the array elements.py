# 04 March 2024
# Swap the array elements

class Solution:
    def swapElements(self, arr, n):
        #Code here
        for i in range(0, n-2):
            arr[i], arr[i+2] = arr[i+2], arr[i]
	        
	return arr
