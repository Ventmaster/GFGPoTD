# 02 December
# Inorder Traversal and BST 

class Solution:
    def isRepresentingBST(self, arr, N):
        return 1 if all(arr[i-1] < arr[i] for i in range(1,N)) else 0
