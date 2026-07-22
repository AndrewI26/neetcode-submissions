# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = node = ListNode()
        while l1 and l2:
            res = l1.val + l2.val + carry
            if res >= 10:
                node.next = ListNode(res - 10)
                carry = 1
            else:
                node.next = ListNode(res)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            node = node.next
        
        while l1:
            node.next = ListNode(l1 + carry)
            carry = 0
            l1 = l1.next
            node = node.next
        while l2:
            node.next = ListNode(l2 + carry)
            carry = 0
            l2 = l2.next
            node = node.next

        if carry != 0:
            node.next = ListNode(carry)

        return dummy.next
