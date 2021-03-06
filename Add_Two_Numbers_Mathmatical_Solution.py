"""2. Add Two Numbers
Medium

12020

2819

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addtwonumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        current_new = new_list
        carry = 0
        while l1.next is not None or l2.next is not None:
            current_new.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0
            current_new.next = ListNode()
            current_new = current_new.next
        current_new.val = (l1.val + l2.val + carry) % 10
        carry = (l1.val + l2.val + carry) // 10
        if carry == 1:
            current_new.next = ListNode(carry)
        return new_list


def list_node_from_list(list_to_convert) -> ListNode:
    list_node = ListNode()
    if list_to_convert:
        list_node.val = list_to_convert[0]
        list_to_convert.pop(0)
    if list_to_convert:
        list_node.next = list_node_from_list(list_to_convert)
    return list_node


my_l1 = [9,9,9,9,9,9,9]
my_l2 = [9,9,9,9]
my_ln1 = list_node_from_list(my_l1)
my_ln2 = list_node_from_list(my_l2)
solution = Solution()
print(solution.addtwonumbers(my_ln1, my_ln2))
print('home')
