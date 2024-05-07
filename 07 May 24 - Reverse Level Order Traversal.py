# 07 May 2024
# Reverse Level Order Traversal

def reverseLevelOrder(root):
    # code here
    li, nums = [], []
    temp = root
    
    li.append(temp)
    
    while li:
        temp = li.pop(0)
        
        if temp.right:
            li.append(temp.right)
        if temp.left:
            li.append(temp.left)
            
        nums.append(temp.data)
        
    return nums[::-1]
