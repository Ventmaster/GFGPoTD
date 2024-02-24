# 24 February 2024
# Maximum Sum

class Solution:
    def maxSum(self, n):
        if n < 6:
            return n
       
        # Dictionary to store computed results
        dp = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}  
       
        # Recursive function to find the maximum sum
        def recursive(n):
            if n in dp:
                return dp[n]
            if n <= 0:
                return 0
           
            # Recursively find the maximum sum for each subproblem
            e1 = recursive(n // 2)
            e2 = recursive(n // 3)
            e3 = recursive(n // 4)
           
            # Store the maximum sum for current subproblem
            dp[n] = max(n, e1 + e2 + e3)
            return dp[n]
       
        return recursive(n)
