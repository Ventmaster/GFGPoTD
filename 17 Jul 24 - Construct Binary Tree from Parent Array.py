# 17th July 2024
# Construct Binary Tree from Parent Array

class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        n = len(parent)
        nodes = [Node(i) for i in range(n)]
        root = None
        
        for i in range(n):
            if parent[i] == -1:
                root = nodes[i]
            else:
                if nodes[parent[i]].left is None:
                    nodes[parent[i]].left = nodes[i]
                else:
                    nodes[parent[i]].right = nodes[i]
                    
        return root
