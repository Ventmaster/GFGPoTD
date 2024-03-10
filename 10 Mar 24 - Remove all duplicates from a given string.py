# 10 March 2024
# Remove all duplicates from a given string

class Solution:
    def removeDuplicates(self,str):
        # code here
	li = list(str)
	result = []
	    
	[result.append(x) for x in li if x not in result]
	str = "".join(result)
        return str
