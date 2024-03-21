# 21 March 2024
# ZigZag Tree Traversal

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        queue = [[root]]
        answer = []
        check = False
        
        while len(queue) != 0:
            temporary = queue.pop()
            nodes = []
            value = []
            
            for one in temporary:
                value.append(one.data)
                
                if one.left:
                    nodes.append(one.left)
                if one.right:
                    nodes.append(one.right)
                    
            if len(nodes) > 0:
                queue.append(nodes)
            
            if check:
                answer.extend(value[::-1])
                check = False
                continue
            
            check = True
            answer.extend(value)
            
        return answer
