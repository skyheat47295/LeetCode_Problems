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
        if not root:
            return False
        elif root and not root.left and not root.right:
            if targetSum - root.val == 0:
                return True
            return False
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


""" Test1 answer True """
my_tree = TreeNode(5, 4, 8)
my_tree.left = TreeNode(4, 11, None)
my_tree.left.left = TreeNode(11, 7, 2)
my_tree.left.left.left = TreeNode(7)
my_tree.left.left.right = TreeNode(2)
my_tree.right = TreeNode(8, 13, 4)
my_tree.right.left = TreeNode(13)
my_tree.right.right = TreeNode(4, None, 1)
my_tree.right.right.right = TreeNode(1)


solution = Solution()
print(solution.hasPathSum(my_tree, 22))
