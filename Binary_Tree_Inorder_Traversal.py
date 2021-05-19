"""94. Binary Tree Inorder Traversal
Easy

4733

216

Add to List

Share
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inordertraversal(self, root: TreeNode) -> list[int]:
        result = []
        if not root:
            return []

        def helper(node):
            if node:
                helper(node.left)
                result.append(node.val)
                helper(node.right)
            return result
        helper(root)
        return result


""" Test  """
my_tree = TreeNode(3, 1, None)
my_tree.left = TreeNode(1, None, 2)
# my_tree.right = TreeNode(2, 3, None)
# my_tree.left.left = TreeNode(3, 4, 4)
# my_tree.left.left.left = TreeNode(4)
# my_tree.left.left.right = TreeNode(4)
my_tree.left.right = TreeNode(2)
# my_tree.right.left = TreeNode(3)
# my_tree.right.right = TreeNode(7)

solution = Solution()
print(solution.inordertraversal(my_tree))
