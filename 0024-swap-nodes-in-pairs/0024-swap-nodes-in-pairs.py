# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head.next)
        node = head
        pre = None
        while node and node.next:
            nx = node.next
            node.next, nx.next = nx.next, node
            if pre:
                pre.next = nx
            
            pre = node
            node = node.next
        return dummy.next
        