# 01 November 2023
# Frequencies of Limited Range Array Elements

import collections

class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        cnt = collections.Counter(arr)
        
        for i in range(1, N+1):
            arr[i-1] = cnt[i]
