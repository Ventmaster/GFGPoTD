# 05 July 2024
# Vertical Width of a Binary Tree

def verticalWidth(root):
    # code here
    if root is None:
        return 0
        
    def dfs(node, head, result):
        if node is None:
            return
        
        result.add(head)
        
        if node.left:
            dfs(node.left, head - 1, result)
        if node.right:
            dfs(node.right, head + 1, result)
            
    result = set()
    dfs(root, 0, result)

    return len(result)
