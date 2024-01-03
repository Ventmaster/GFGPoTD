# 03 January 2024
# Smallest window containing 0, 1 and 2

class Solution:
    def smallestSubstring(self, S):
        # Code here
        if '0' not in S or '1' not in S or '2' not in S:
            return -1 
            
        li = []
        x = 10**5 + 1
        
        for i in S:
            if li == []:
                li.append(i)
            elif li[0] != i:
                li.append(i)
            elif li[0] == i:
                li.pop(0)
                li.append(i)
                j = 1
                
                while (len(li) > 1 and j):
                    if (li[0] == li[1]):
                        li.pop(0)
                    else:
                        j = 0
            
            if '0' in li and '1' in li and '2' in li:
                x = min(x, len(li))
                li = []
                
        return x
