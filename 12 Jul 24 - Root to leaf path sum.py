# 12th July 2024
# Root to leaf path sum

class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # code here
        if root == None:
            return False
            
        if root.left == None and root.right == None:
            return root.data == target
            
        return self.hasPathSum(root.left, target - root.data) or self.hasPathSum(root.right, target - root.data)
