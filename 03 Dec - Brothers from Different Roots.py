# 03 Dec 2023
# Brothers from Different Roots

class Solution:
   
    def countPairs(self, root1, root2, target_sum):
        nodes_set_1, nodes_set_2 = set(), set()

        def inorder_traversal(node, tree_number):
            if not node:
                return

            inorder_traversal(node.left, tree_number)

            if tree_number == 1:
                nodes_set_1.add(node.data)
            else:
                nodes_set_2.add(node.data)

            inorder_traversal(node.right, tree_number)

        # Perform inorder traversal for both BSTs
        inorder_traversal(root1, 1)
        inorder_traversal(root2, 0)

        result_count = 0

        # Count pairs with the given sum
        for value in nodes_set_1:
            result_count += 1 if target_sum - value in nodes_set_2 else 0

        return result_count
