# 02 February 2024
# Implement Atoi

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        try:
            return int(s)
        except:
            return -1
