# 14 January 2024
# Find duplicate rows in a binary matrix

class Solution:
    def repeatedRows(self, arr, m ,n):
    #code here
    d, answer = {}, []

    for row in range(m):
        add = sum(arr[row])
            
        if add not in d:
            d[add] = {}
            d[add][row] = arr[row]
        else:
            for i in d[add]:
                if d[add][i] == arr[row]:
                    answer.append(row)
                    break
                
            d[add][row] = arr[row]
            
    return answer
