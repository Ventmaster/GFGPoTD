# 04 July 2024
# Duplicate Subtrees

from collections import defaultdict

class Solution:
    def printAllDups(self, root):
        ans = [] 
        d = defaultdict(int)  

        def traverse(node):
            if not node:
                return ""

            path = str(node.data) + traverse(node.left) + traverse(node.right)

            d[path] += 1

            if d[path] == 2:
                ans.append(node)

            return path

        traverse(root)
        return ans
