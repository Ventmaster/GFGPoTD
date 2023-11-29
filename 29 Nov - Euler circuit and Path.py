# 29 November 2023
# Euler circuit and Path

class Solution:
    def isEulerCircuitExist(self, V, adj):
        even = 0
        odd = 0

        for i in range(V):
            if len(adj[i]) % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1

        if V == even:
            return 2

        if odd == 2:
            return 1

        return 0
