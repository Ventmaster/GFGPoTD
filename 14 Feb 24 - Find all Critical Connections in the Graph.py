# 14 February 2024
# Find all Critical Connections in the Graph

class Solution:
    def criticalConnections(self, V, adj):
        # code here
        
        disc = [-1 for i in range(V)]
        low = [-1 for i in range(V)]
        self.time = 0
        bridges = []

        def SCC(u, par = -1):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1

            for v in adj[u]:
                if v == par:
                    continue
                if disc[v] == -1:
                    SCC(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        if v > u:
                            bridges.append([u, v])
                        else:
                            bridges.append([v, u])
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if disc[i] == -1:
                SCC(i)
        bridges.sort()
        return bridges
