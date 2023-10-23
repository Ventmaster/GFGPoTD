# 23 October 2023
# Maximum sum increasing subsequence

class Solution:
    def maxSumIS(self, Arr, n):
        # code here
	if n == 0:
            return 0
	    
    	dp = [0] * n
	dp[n-1] = Arr[n-1]
		
    	for i in reversed(range(n-1)):
    	    maxSum = 0
		    
	    for j in range(i+1, n):
		if Arr[j] > Arr[i]:
		    maxSum = max(maxSum, dp[j])
                
                dp[i] = Arr[i] + maxSum
                
        return max(dp)
