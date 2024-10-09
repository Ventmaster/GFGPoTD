# 09th October 2024
# Linked List Matrix

class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        n = len(mat)
        prev_row_head = None
        curr_row_head = None
        prev = None
        head = None
        
        for i in range(n):
            for j in range(n):
                if j == 0:
                    if i == 0:
                        head = Node(mat[i][j])
                        prev = head
                    else:
                        prev = Node(mat[i][j])
                        
                    curr_row_head = prev
                
                else:
                    prev.right = Node(mat[i][j])
                    prev = prev.right
                    
                if i != 0:
                    prev_row_head.down = prev
                    prev_row_head = prev_row_head.right
                    
                if j == n-1:
                    prev_row_head = curr_row_head
                    
        return head
