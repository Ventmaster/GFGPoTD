# 02nd June 2024
# Construct list using given q XOR queries

from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # code here
        xor = 0
        li = []
        
        while queries:
            a, b = queries.pop()
            
            if a == 0:
                li.append(b ^ xor)
            else:
                xor ^= b
                
        li.append(xor)
        return sorted(li)
