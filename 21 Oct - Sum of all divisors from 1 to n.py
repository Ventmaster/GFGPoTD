# 21 October 2023
# Sum of all divisors from 1 to n

class Solution:
    def sumOfDivisors(self, N):
    	#code here 
    	sum = 0
    	
    	for i in range(1, N+1):
    	    num = N // i
    	    sum1 = num * i
    	    sum += sum1
    	    
        return sum
