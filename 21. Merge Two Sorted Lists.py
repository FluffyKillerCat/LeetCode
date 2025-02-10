# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(0)
    head = list1
    list2 = ListNode(0)
    head_2 = list2
    """creating ListNodes to test"""
    for i in range(100):
        head.next = ListNode(i)
        head = head.next

        head_2.next = ListNode(i * -1)
        head_2 = head_2.next
    ans = s.mergeTwoLists(list1, list2)
    while ans:
        print(ans.val)
        ans = ans.next