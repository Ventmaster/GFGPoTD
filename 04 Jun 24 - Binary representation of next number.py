# 04th June 2024
# Binary representation of next number

class Solution:
    def binaryNextNumber(self, s):
        # code here
	s = int(s, 2)
	return bin(s+1)[2:]
