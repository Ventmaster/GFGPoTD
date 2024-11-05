# 05th November 2024
# Rotate by 90 degree

def rotate(mat): 
    #code here
    n = len(mat)
    temp = 0
    
    for i in range(n):
        for j in range(i,n):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
            
    for i in mat:
        i.reverse()
