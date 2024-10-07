# 07th October 2024
# XOR Linked List

def insert(head, data):
    node = Node(data)
    
    if head == None:
        head = node
    else:
        node.npx = head
        head = node
        
    return head
    
def getList(head):
    li = []
    
    while head:
        li.append(head.data)
        head = head.npx
    
    return li
