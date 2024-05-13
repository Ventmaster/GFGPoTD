# 13th May 2024
# Number of Good Components

from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # code here
        parent = list(range(v))
        degree = [0] * v
        group = defaultdict(list)
        
        def finding_parent(x: int) -> int:
            if parent[x] == x:
                return x
            parent[x] = finding_parent(parent[x])
            return parent[x]
            
        for x, y in edges:
            degree[x-1] += 1
            degree[y-1] += 1
            parent[finding_parent(x-1)] = finding_parent(y-1)
            
        for i in range(v):
            group[finding_parent(i)].append(i)
            
        return sum(all(degree[x] == len(comps) - 1 for x in comps) for comps in group.values())
