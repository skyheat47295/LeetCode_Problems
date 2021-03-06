"""104. Maximum Depth of Binary Tree
Easy

3746

95

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxdepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))
        else:
            return 0


""" Test1 answer 3
my_tree = TreeNode(3, 9, 20)
my_tree.left = TreeNode(9, None, None)
my_tree.right = TreeNode(20, 15, 7)
# my_tree.left.left = TreeNode(3)
# my_tree.left.right = TreeNode(4)
my_tree.right.left = TreeNode(15)
my_tree.right.right = TreeNode(7)
"""

""" Test2 answer 2
my_tree = TreeNode(1, None, 2)
#my_tree.left = TreeNode(9, None, None)
my_tree.right = TreeNode(2)
# my_tree.left.left = TreeNode(3)
# my_tree.left.right = TreeNode(4)
#my_tree.right.left = TreeNode(15)
#my_tree.right.right = TreeNode(7)
"""

""" Test3 answer 1
my_tree = TreeNode(0)
#my_tree.left = TreeNode(9, None, None)
#my_tree.right = TreeNode(2)
# my_tree.left.left = TreeNode(3)
# my_tree.left.right = TreeNode(4)
#my_tree.right.left = TreeNode(15)
#my_tree.right.right = TreeNode(7)
"""
solution = Solution()
print(solution.maxdepth(my_tree))
