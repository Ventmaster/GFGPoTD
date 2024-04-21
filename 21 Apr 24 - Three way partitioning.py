# 21 April 2024
# Three way partitioning

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    # code here 
	    left, middle, right = [0, 0, len(array)-1]
	    
	    while middle <= right:
	        if array[middle] < a:
	            array[left], array[middle] = array[middle], array[left]
                left += 1
                middle += 1
            elif array[middle] > b:
                array[right], array[middle] = array[middle], array[right]
                right -= 1
            else:
                middle += 1
                
        return array
