# 20 January 2024
# Distribute candies in a binary tree

class Solution:
    def distributeCandy(self, root):
        #code here
        self.moves = 0
        
        def dfs(root):
            if not root:
                return 0
                
            l = dfs(root.left)
            r = dfs(root.right)
            
            self.moves += abs(l) + abs(r)
            rem = l + r + root.data - 1
            
            return rem
            
        dfs(root)
        return self.moves
