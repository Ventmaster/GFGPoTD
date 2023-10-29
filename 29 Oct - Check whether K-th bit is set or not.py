# 29 October 2023
# Check whether K-th bit is set or not

class Solution:
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        if ((n>>k)%2 == 1):
            return 1
        else:
            return 0 
