"""145. Binary Tree Postorder Traversal
Easy

2629

118

Add to List

Share
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
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
Output: [2,1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        if not root:
            return []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                result.append(node.val)
            return result

        helper(root)
        return result

import binarytree
my_tree = binarytree.build2([1, None, 2])
solution = Solution()
print(solution.postorderTraversal(my_tree))
