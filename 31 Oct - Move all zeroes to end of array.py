# 31 October 2023
# Move all zeroes to end of array

class Solution:
	def pushZerosToEnd(self,arr, n):
	    cnt = 0
	    
	    for i in range(n):
	        if arr[i] != 0:
	            arr[cnt], arr[i] = arr[i], arr[cnt]
	            cnt = cnt + 1
