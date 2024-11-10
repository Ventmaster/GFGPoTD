# 10th November 2024
# Union of Two Sorted Arrays with Distinct Elements

class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        return sorted(set(a) | set(b))
