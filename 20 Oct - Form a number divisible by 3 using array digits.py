# 20 October 2023
# Form a number divisible by 3 using array digits

class Solution:
    def isPossible(self, N, arr):
        # code here
        if sum(arr) % 3 == 0:
            return 1
            
        return 0 
