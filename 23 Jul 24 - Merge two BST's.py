# 23rd July 2024
# Merge two BST's

class Solution:
    def merge(self, root1, root2):
        # code here
        a, b, result = [], [], []
        
        def traversal(root, arr):
            if root == None:
                return 
            
            traversal(root.left, arr)
            arr.append(root.data)
            traversal(root.right, arr)
            
        traversal(root1, a)
        traversal(root2, b)
        n, m = len(a), len(b)
        l, r = 0, 0
        
        while l < n and r < m:
            if a[l] <= b[r]:
                result.append(a[l])
                l += 1
            elif a[l] > b[r]:
                result.append(b[r])
                r += 1
                
        if l == n:
            result.extend(b[r:m])
        else:
            result.extend(a[l:n])
            
        return result
