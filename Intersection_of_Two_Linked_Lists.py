"""160. Intersection of Two Linked Lists
Easy

5684

640

Add to List

Share
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getintersectionnode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list1, list2 = headA, headB
        while list1 != list2:
            list1 = list1.next if list1 else headB
            list2 = list2.next if list2 else headA
        return list1


def list_node_from_list(list_to_convert) -> ListNode:
    list_node = ListNode(None)
    if list_to_convert:
        list_node.val = list_to_convert[0]
        list_to_convert.pop(0)
    if list_to_convert:
        list_node.next = list_node_from_list(list_to_convert)
    return list_node


listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
my_list_nodeA = list_node_from_list(listA)
my_list_nodeB = list_node_from_list(listB)
intersection2 = my_list_nodeA.next
intersection1 = my_list_nodeB.next.next
my_list_nodeA.next = my_list_nodeB.next.next
solution = Solution()
result = solution.getintersectionnode(my_list_nodeA, my_list_nodeB)
print(result)
