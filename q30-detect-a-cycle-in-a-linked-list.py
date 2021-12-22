# Solution 1:
# Space: O(n)
# We will traverse each node and store it in the set. So that when we get that node in future. We can say that the linkedlist has cycle or circluar.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        s = set()
        while head:
            if head in s: return True
            s.add(head)
            head = head.next
        return False

# Solution 2:
# optimised O(1) space
# Think of two cars one with 2x speed than other.
# In our childhood we have solved those type of question where we have to find in how many revolution they will meet again.
# Obvioulsy this condition can only be possible when the track is circular right?
# So the same logic we are doing here.
# we took fast and slow cars here and will continue to traverse in the linkedlist.
# If they meet again,we can say track was circular,
# If it get null at the end, we can say that track was parallel.

# Hope I am able to explain it well.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False