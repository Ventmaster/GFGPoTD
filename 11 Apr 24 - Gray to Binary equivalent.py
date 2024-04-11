# 11 April 2024
# Gray to Binary equivalent

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        b = bin(n)[2:]
        previous = int(b[0])
        result = str(previous)
        
        for i in range(1, len(b)):
            x = previous ^ int(b[i])
            result += str(x)
            previous = x
            
        return int(result, 2)
