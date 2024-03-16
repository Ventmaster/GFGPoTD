# 16 March 2024
# Delete without head pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        #code here
        if del_node.next == None:
            return
        else:
            prev = del_node
            curr = del_node.next
            temp = del_node.next.next
            
            prev.data = curr.data
            prev.next = temp
            
            del curr
