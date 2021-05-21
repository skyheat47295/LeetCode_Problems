"""144. Binary Tree Preorder Traversal
Easy

2319

90

Add to List

Share
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [1,2]
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
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        if not root:
            return []

        def helper(node):
            if node:
                result.append(node.val)
                helper(node.left)
                helper(node.right)
            return result
        helper(root)
        return result


import binarytree
my_tree = binarytree.build2([1, None, 2])
# values = [1, None, 2, 3]
# root = bt.build2(values)
solution = Solution()
print(solution.preorderTraversal(my_tree))
