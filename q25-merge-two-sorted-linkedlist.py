# Leetcose 21

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = None

        while l1 and l2:
            min_node = l1
            if l1.val < l2.val: l1 = l1.next
            else:
                min_node = l2
                l2 = l2.next
            if head == None: head = min_node
            else: prev.next = min_node
            prev = min_node

        if l1:
            if head == None: head = l1
            else: prev.next = l1
        if l2:
            if head == None: head = l2
            else: prev.next = l2
        return head