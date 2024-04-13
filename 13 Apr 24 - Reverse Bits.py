# 13 April 2024
# Reverse Bits

class Solution:
    def reversedBits(self, x):
        # code here 
        rb = format(x, '032b')
        rb = rb[::-1]
        return int(rb, 2)
