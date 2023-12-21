# 21 December 2023
# Candy

class Solution:
    def minCandy(self, N, ratings):
        # Code here
        candies = [1] * N 
        
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
                
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
                
        total_candies = sum(candies)
        
        return total_candies
