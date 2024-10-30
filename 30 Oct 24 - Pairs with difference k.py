# 30th October 2024
# Pairs with difference k

class Solution:
    def countPairsWithDiffK(self, arr, k):
        # Initialize variables
        i, j, n = 0, 1, len(arr)
        arr.sort()
        ans = 0
        
        # Loop through the sorted array
        while j < n:
            diff = arr[j] - arr[i]
            
            if diff == k:
                countI, countJ = 1, 1
                
                # Count occurrences of arr[i]
                while i < n - 1 and arr[i] == arr[i + 1]:
                    countI += 1
                    i += 1
                
                # Count occurrences of arr[j]
                while j < n - 1 and arr[j] == arr[j + 1]:
                    countJ += 1
                    j += 1
                
                # Add pair combinations to the answer
                ans += (countI * countJ)
                
                # Move both pointers forward
                i += 1
                j += 1
            
            elif diff < k:
                j += 1
            else:
                i += 1
        
        return ans
