# 01 July 2024
# Make Binary Tree From Linked List

from collections import deque

def convert(head):
    # code here
    if head.next == None:
        return Tree(head.data)
        
    queue = deque()
    root = Tree(head.data)
    queue.append(root)
    
    head = head.next
    
    while head:
        current = queue.popleft()
        current.left = Tree(head.data)
        queue.append(current.left)
        head = head.next
        
        if head:
            current.right = Tree(head.data)
            queue.append(current.right)
            head = head.next
            
    return root
