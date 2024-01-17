# 17 January 2024
# All Unique Permutations of an array

from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        # code here
        answer = list(set(permutations(arr, n)))
        return sorted(answer)
