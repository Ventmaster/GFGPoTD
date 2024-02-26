# 26 February 2024
# Power Set

from itertools import combinations

class Solution:
    def AllPossibleStrings(self, s):
        # Code here
	result = []
		
	for i in range(1, len(s)+1):
            for j in list(combinations(s,i)):
                result.append("".join(j))
		
	result.sort()
		
	return result
