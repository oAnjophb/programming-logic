
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode):
        nextHead = head.next

        newListNode:ListNode = []

        for num in head:
            if num != nextHead:
                newListNode.append(num)

        return newListNode.val, newListNode.next
    
s = Solution()

nodes = ListNode()
print(s.deleteDuplicates([1,1,2,3,3]))