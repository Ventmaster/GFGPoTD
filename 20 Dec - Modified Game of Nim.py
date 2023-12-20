# 20 December
# Modified Game of Nim

class Solution:
    def findWinner(self, n, A):
        # code here
        answer = 0
        
        for a in A:
            answer ^= a
        
        winner = 1 if answer == 0 else (n%2) + 1
        return winner
