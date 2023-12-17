# 17 December 2023
# Max Sum without Adjacents

class Solution:
    def findMaxSum(self,arr, n):
        # code here
        if n == 0:
            return 0
	if n == 1:
	    return arr[0]
		
	inclusive = arr[0]
	exclusive = 0
		
	for i in range(1,n):
            new_exclusive = max(inclusive, exclusive)
	    inclusive = exclusive + arr[i]
	    exclusive = new_exclusive
		
	return max(inclusive, exclusive)
