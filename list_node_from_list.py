# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_node_from_list(list_to_convert) -> ListNode:
    list_node = ListNode(None)
    if list_to_convert:
        list_node.val = list_to_convert[0]
        list_to_convert.pop(0)
    if list_to_convert:
        list_node.next = list_node_from_list(list_to_convert)
    return list_node


listA = [4, 1, 8, 4, 5]
my_list_node = list_node_from_list(listA)
print(my_list_node)
