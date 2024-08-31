# 31st August 2024
# Sorted subsequence of size 3

class Solution:
    def find3Numbers(self, arr):
        # Code Here
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    for k in range(j + 1, len(arr)):
                        if arr[j] < arr[k]:
                            return [arr[i], arr[j], arr[k]]
        
        return []
