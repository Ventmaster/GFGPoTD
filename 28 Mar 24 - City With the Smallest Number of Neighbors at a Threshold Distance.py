# 28 March 2024
# City With the Smallest Number of Neighbors at a Threshold Distance

from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        # code here
        d = defaultdict(list)
        
        for u, v, w in edges:
            d[u].append((v,w))
            d[v].append((u,w))
            
        def dijkstra(n):
            costs = {n: 0}
            q = [(0, n)]
            
            while q:
                cost0, n0 = heappop(q)
                
                for nbr, c in d[n0]:
                    cost = cost0 + c
                    
                    if cost > distanceThreshold:
                        continue
                    
                    if nbr not in costs or costs[nbr] > cost:
                        costs[nbr] = cost
                        heappush(q, (cost, nbr))
                        
            return len(costs)
            
        result = 0
        count = n
        
        for k in range(n):
            c = dijkstra(k)
            
            if c <= count:
                count = c
                result = k
                
        return result
