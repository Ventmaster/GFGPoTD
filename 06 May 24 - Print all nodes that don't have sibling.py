# 06 May 2024
# Print all nodes that don't have sibling

from collections import deque

def noSibling(root):
    # code here
    result = []
    q = deque([root])
    
    while q:
        top = q.popleft()
    
        if top.left:
            q.append(top.left)
            
            if top.right:
                q.append(top.right)
            else:
                result.append(top.left.data)
                
        elif top.right:
            result.append(top.right.data)
            q.append(top.right)
            
    return [-1] if not result else sorted(result)
