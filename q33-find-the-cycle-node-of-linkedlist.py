class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        if not slow or not slow.next: return None
        fast = slow.next
        
        while fast and fast.next:
            if slow == fast:
                itr, slow = head, slow.next
                while True:
                    if itr == slow: return itr
                    itr = itr.next
                    slow = slow.next
                    
            slow = slow.next
            fast = fast.next.next
        return None