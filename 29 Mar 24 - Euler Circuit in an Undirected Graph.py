# 29 March 2024
# Euler Circuit in an Undirected Graph

from collections import Counter

class Solution:
    def isEularCircuitExist(self, v, adj):
        #Code here
	li = []
		
	for i in adj:
            li += i
		    
	count = Counter(li)
		
	for i in count.keys():
	    if count[i] % 2 == 1:
                return 0
		        
	return 1
