# 19 March 24
# Possible Paths in a Tree

class Solution:
    def maximumWeight(self, n, edges, q, queries):
        # code here
        a = list(range(n))
        y = [1] * n
        
        def find(u):
            if a[u] != u:
                a[u] = find(a[u])
            return a[u]
        
        edges.sort(key = lambda x: x[2], reverse = True)
        queries = sorted(enumerate(queries), key = lambda x:x[1])
        
        answer = [0] * q
        curr = 0
        
        for index, x in queries:
            while edges and edges[-1][2] <= x:
                u, v, _ = edges.pop()
                u, v = find(u-1), find(v-1)
                
                if u != v:
                    a[u] = v
                    curr += y[u] * y[v]
                    y[v] += y[u]
                    
            answer[index] = curr
            
        return answer
