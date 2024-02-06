# 06 February 2024
# Count the nodes at distance K from leaf

class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        #code here
        result = set()
        path = []
        
        def dfs(node):
            if not node:
                return
            
            path.append(node)
            
            if not node.left and not node.right:
                if len(path) > k:
                    result.add(path[-(k+1)])
                    
            dfs(node.left)
            dfs(node.right)
            
            path.pop()
            
        dfs(root)
        
        return len(result)
