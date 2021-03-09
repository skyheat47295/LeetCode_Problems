"""
83. Remove Duplicates from Sorted List
Easy

2327

143

Add to List

Share
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteduplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        in_head = head
        while in_head.next:
            if in_head.val == in_head.next.val:
                in_head.next = in_head.next.next
            else:
                in_head = in_head.next
        return head  # difference in returning head vs in_head


my_head = ListNode(1)
my_head.next = ListNode(1)
my_head.next.next = ListNode(2)
# my_head.next.next.next = ListNode(3)
# my_head.next.next.next.next = ListNode(3)

solution = Solution()
solution.deleteduplicates(my_head)
print('done')
