# 28 November 2023
# Sum of dependencies in a graph

class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        sum = 0
        
        for i in adj:
            sum = sum + len(i)
            
        return sum
