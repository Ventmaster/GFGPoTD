# 02 May 2024
# Serialize and deserialize a binary tree

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.data)
                inorder(root.right, result)
        
        result = []
        inorder(root, result)
        
        return result
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
        def func(a, left, right):
            if left > right:
                return
            
            index = (left + right) // 2
            root = Node(a[index])
            root.left = func(a, left, index-1)
            root.right = func(a, index+1, right)
            
            return root
            
        return func(a, 0, len(a)-1)
