"""112. Path Sum
Easy

3033

603

Add to List

Share
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        pass


""" Test1 answer 2
my_tree = TreeNode(3, 9, 20)
my_tree.left = TreeNode(9, None, None)
my_tree.right = TreeNode(20, 15, 7)
# my_tree.left.left = TreeNode(3)
# my_tree.left.right = TreeNode(4)
my_tree.right.left = TreeNode(15)
my_tree.right.right = TreeNode(7)
"""

""" Test2 answer 5 """
my_tree = TreeNode(2, None, 3)
my_tree.right = TreeNode(3, None, 4)
my_tree.right.right = TreeNode(4, None, 5)
my_tree.right.right.right = TreeNode(5, None, 6)
my_tree.right.right.right.right = TreeNode(6)


solution = Solution()
print(solution.hasPathSum(my_tree, 22))

