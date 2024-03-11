# 11 March 2024
# Count pairs Sum in matrices

class Solution:
    def countPairs(self, mat1, mat2, n, x):
        i = [0, 0]
        j = [n-1, n-1]
        count = 0

        while (i[0] != n and j[0] != -1):
            if mat1[i[0]][i[1]] + mat2[j[0]][j[1]] == x:
                count += 1
                i[1] += 1
                j[1] -= 1
            elif mat1[i[0]][i[1]] + mat2[j[0]][j[1]] > x:
                j[1] -= 1
            elif mat1[i[0]][i[1]] + mat2[j[0]][j[1]] < x:
                i[1] += 1

            if i[1] == n:
                i[0] += 1
                i[1] = 0

            if j[1] == -1:
                j[0] -= 1
                j[1] = n-1

        return count
