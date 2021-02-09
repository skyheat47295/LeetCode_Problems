"""
21. Merge Two Sorted Lists
Easy

6056

720

Add to List

Share
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_list = new_list_result = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                new_list.next = l2
                l2 = l2.next
            else:
                new_list.next = l1
                l1 = l1.next
            new_list = new_list.next

        if l1:
            new_list.next = l1
        if l2:
            new_list.next = l2
        return new_list_result.next


my_l1 = []
# my_l1.next = ListNode(2)
# my_l1.next.next = ListNode(4)

my_l2 = [0]
# my_l2.next = ListNode(3)
# my_l2.next.next = ListNode(4)
solution = Solution()

print(solution.mergeTwoLists(my_l1, my_l2))
