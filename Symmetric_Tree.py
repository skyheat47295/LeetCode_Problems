"""101. Symmetric Tree
Easy

5820

155

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def issymmetric(self, root: TreeNode) -> bool:
        def stage_2(left, right):
            if right is None and left is None:
                return True
            elif left and right:
                return left.val == right.val and \
                       stage_2(left.left, right.right) and \
                       stage_2(left.right, right.left)
            else:
                return False

        if root:
            return stage_2(root.left, root.right)
        else:
            return True


""" Test3 True """
my_tree = TreeNode(1, 2, 2)
my_tree.left = TreeNode(2)
my_tree.right = TreeNode(2)
#my_tree.left.left = TreeNode(3)
#my_tree.left.right = TreeNode(4)
#my_tree.right.left = TreeNode(4)
#my_tree.right.right = TreeNode(3)

""" Test2 False
my_tree = TreeNode(1, 2, 2)
my_tree.left = TreeNode(2, None, 3)
my_tree.right = TreeNode(2, None, 3)
#  my_tree.left.left = TreeNode(3)
my_tree.left.right = TreeNode(3)
#  my_tree.right.left = TreeNode(4)
my_tree.right.right = TreeNode(3)
"""

""" Test1 True
my_tree = TreeNode(1, 2, 2)
my_tree.left = TreeNode(2, 3, 4)
my_tree.right = TreeNode(2, 4, 3)
my_tree.left.left = TreeNode(3)
my_tree.left.right = TreeNode(4)
my_tree.right.left = TreeNode(4)
my_tree.right.right = TreeNode(3)
"""

"""https://realpython.com/null-in-python/"""


solution = Solution()
print(solution.issymmetric(my_tree))
