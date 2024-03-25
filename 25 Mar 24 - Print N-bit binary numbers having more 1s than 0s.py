# 25 March 2024
# Print N-bit binary numbers having more 1s than 0s

class Solution:
    def NBitBinary(self, n):
        # code here
	pos = 0
		
	binary_no = [["", 0, 0]]
		
	while pos < n:
	    new_binary_no = []
		    
	    for binary, count_0, len_binary in binary_no:
		new_binary_no.append([binary+"1", count_0, len_binary+1])
		        
		if count_0 * 2 < len_binary:
		    new_binary_no.append([binary+"0", count_0+1, len_binary + 1])
		            
	    pos += 1
	    binary_no = new_binary_no[:]
		    
	return [binary for binary, _, _ in binary_no]
