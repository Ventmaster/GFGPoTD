# 23rd August 2024
# Left View of Binary Tree

#Function to return a list containing elements of left view of the binary tree.

from collections import deque

def LeftView(root):
    # code here
    que=deque([root])
    res=[]
    
    while que:
        n,i=len(que),0
        
        for _ in range(n):
            cur=que.popleft()
            
            if i==0:
                res.append(cur.data)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
                
            i+=1
    return res
