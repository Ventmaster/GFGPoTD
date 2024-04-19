# 19 April 2024
# Find missing in second array

class Solution:
    def findMissing(self,a,b,n,m):
        new_set = set()
        li = []
        
        for num in b:
            new_set.add(num)
        
        for num in a:
            if num not in new_set:
                li.append(num)
        
        return li
