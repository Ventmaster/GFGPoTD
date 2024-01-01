# 01 January 2024
# Array Pair Sum Divisibility Problem

#User function Template for python3

class Solution:
    def canPair(self, nuns, k):
        # Code here
	n = len(nums)
		
    	if n % 2 == 1:
            return False
	    
	s = set()
		
	for i in range(n):
	    if (k - nums[i]) % k in s:
                s.remove((k - nums[i]) % k)
            else:
                s.add(nums[i]%k)
        
        return False if s else True
