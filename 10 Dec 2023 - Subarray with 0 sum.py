# 10 December 2023
# Subarray with 0 sum

class Solution:
    def subArrayExists(self, arr, n):
        sum = 0
        s = set()

        for i in range(n):
            sum += arr[i]
            if sum == 0 or sum in s:
                return True
            s.add(sum)

        return False 
