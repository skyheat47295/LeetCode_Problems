"""111. Minimum Depth of Binary Tree
Easy

2327

809

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mindepth(self, root: TreeNode) -> int:
        if root:
            if not root.left:  # root node is not a leaf node, so need to create an exception
                return 1 + self.mindepth(root.right)
            elif not root.right:
                return 1 + self.mindepth(root.left)
            else:
                return 1 + min(self.mindepth(root.left), self.mindepth(root.right))
        else:
            return 0


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
print(solution.mindepth(my_tree))
