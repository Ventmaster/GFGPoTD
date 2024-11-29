# 29th November 2024
# Add Binary Strings

class Solution:
    def addBinary(self, s1, s2):
        # code here
	S1 = int(s1, 2)
    	S2 = int(s2, 2)

    	return bin(S1 + S2)[2:]
