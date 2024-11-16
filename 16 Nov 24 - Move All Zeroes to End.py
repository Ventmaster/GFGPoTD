# 16th November 2024
# Move All Zeroes to End

class Solution:
    def pushZerosToEnd(self, arr):
        # code here
        temporary = []
        count_of_zeroes = 0
        
        for i in range(len(arr)):
            if arr[i] == 0:
                count_of_zeroes += 1
            else:
                temporary.append(arr[i])
        
        result = temporary + [0] * count_of_zeroes
        
        for i in range(len(result)):
            arr[i] = result[i]
