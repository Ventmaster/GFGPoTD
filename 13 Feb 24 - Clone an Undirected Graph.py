# 13 February 2024
# Clone an Undirected Graph

from sys import setrecursionlimit

class Solution():
    def cloneGraph(self, node):
        #your code goes here
        setrecursionlimit(10**4)
        
        cur = dict()
        q = [node]
        
        while q:
            curr = q.pop()
            cur[curr] = Node()
            
            for next in curr.neighbors:
                if next not in cur:
                    q.append(next)
                    
        for x, y in cur.items():
            y.val = x.val
            y.neighbors = [cur[x] for x in x.neighbors]
            
        return cur[node]
