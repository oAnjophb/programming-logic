from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current_node = head

        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        current_node.next = list1 if list1 else list2

        return head
    

def to_listnode(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

list1 = [1, 2, 4]
list2 = [1, 3, 4]

ln1 = to_listnode(list1)
ln2 = to_listnode(list2)

sol = Solution()
merged = sol.mergeTwoLists(ln1, ln2)
print(to_list(merged))