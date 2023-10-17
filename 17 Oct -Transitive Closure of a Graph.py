# 17 October 2023
# transitive closure of a graph

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if (graph[i][k] and graph[k][j]) or i == j:
                        graph[i][j] = 1
                        
        return graph 
