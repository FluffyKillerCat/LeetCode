# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
from typing import List, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-101)
        tail = dummy

        while head:

            if tail.val == head.val:
                head = head.next

                continue

            tail.next = ListNode(head.val)
            head = head.next
            tail = tail.next

        return dummy.next




