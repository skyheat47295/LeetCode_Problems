"""110. Balanced Binary Tree
Easy

3358

223

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isbalanced(self, root: TreeNode) -> bool:
        # if not root:
        #    return True

        count_left = 1 + self.isbalanced(root.left) if root.left else 0
        count_right = 1 + self.isbalanced(root.right) if root.right else 0
        print(count_left, count_right)
        return bool(abs(count_left-count_right) <= 1)
        #return bool((max(self.isbalanced(root.left), self.isbalanced(root.right)) + 1) <= 1)

""" Test2 answer False """
my_tree = TreeNode(1, 2, 2)
my_tree.left = TreeNode(2, 3, 3)
my_tree.right = TreeNode(2)
my_tree.left.left = TreeNode(3, 4, 4)
my_tree.left.left.left = TreeNode(4)
my_tree.left.left.right = TreeNode(4)
my_tree.left.right = TreeNode(3)
# my_tree.right.left = TreeNode(15)
# my_tree.right.right = TreeNode(7)

solution = Solution()
print(solution.isbalanced(my_tree))
