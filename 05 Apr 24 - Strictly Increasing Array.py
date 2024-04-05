# 05 April 2024
# Strictly Increasing Array

class Solution:
    def min_operations(self,nums):
        # Code here
	n = len(nums)
	dp = [1] * n
		
	for i in range(n):
	    for j in range(i):
		if nums[i] - nums[j] >= i-j:
		    dp[i] = max(dp[i], dp[j]+1)
		            
	maximum_operation = max(dp)
	    
	return n - maximum_operation
