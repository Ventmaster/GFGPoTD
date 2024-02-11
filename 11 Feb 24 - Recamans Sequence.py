# 11 February 2024
# Recamans Sequence

class Solution:
    def recamanSequence(self, n):
        # code here
        if n < 2:
            return [i for i in range(n)]
            
        visited = {0, 1}
        sequence = [0, 1]
        cur = 1
        
        for i in range(2, n+1):
            cur = cur - i if cur - i > 0 and cur - i not in visited else cur + i
            visited.add(cur)
            sequence.append(cur)
            
        return sequence
