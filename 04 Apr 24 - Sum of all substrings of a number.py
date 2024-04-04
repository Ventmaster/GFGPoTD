# 04 April 2024
# Sum of all substrings of a number

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        # code here
        result = sum_1 = sum_0 = 0
        
        for x, y in enumerate(s):
            sum_1 = (sum_0 * 10 + int(y) * (x+1)) % (10**9+7)
            result = (result + sum_0) % (10**9+7)
            sum_0 = sum_1
            
        return (result + sum_0) % (10**9+7)
