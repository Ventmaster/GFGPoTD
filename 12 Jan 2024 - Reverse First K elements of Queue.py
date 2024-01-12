# 12 January 2024
# Reverse First K elements of Queue

class Solution:
    def modifyQueue(self, q, k):
        # code here
        return q[:k][::-1] + q[k:]
