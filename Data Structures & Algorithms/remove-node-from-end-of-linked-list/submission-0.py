# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ahead = head

        for i in range(n + 1):
            if not ahead:
                return head.next
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            head = head.next
        
        head.next = head.next.next

        return dummy