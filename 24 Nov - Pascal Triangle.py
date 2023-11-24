# 24 November 2023
# Pascal Triangle

class Solution:
    def nthRowOfPascalTriangle(self, n):
        if n == 1:
            return [1]

        modulo = 10**9 + 7
        result = [1, 1]

        if n == 2:
            return result

        for i in range(3, n+1):
            temp = [1] * i

            for j in range(1, i-1):
                temp[j] = (result[j-1] + result[j]) % modulo

            result = temp

        return result 
