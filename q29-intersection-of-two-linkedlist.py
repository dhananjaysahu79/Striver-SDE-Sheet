# Naive solution

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        s = set()
        itr = headA
        
        while itr:
            s.add(itr)
            itr = itr.next
        
        itr = headB
        while itr:
            if itr in s:
                return itr
            itr = itr.next
        return itr

# O(1) space

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        itr1 = headA
        itr2 = headB
        
        while True:
            if itr1 == itr2: return itr1
            
            if not itr1 and not itr2: return None
            if not itr1: itr1 = headB
            if not itr2: itr2 = headA
            if itr1 == itr2: return itr1
            
            itr1 = itr1.next
            itr2 = itr2.next

# O(1) space and reduced lines of code

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        itr1 = headA
        itr2 = headB
        
        while True:
            if itr1 == itr2: return itr1
            if not itr1 and not itr2: return None
            
            itr1 = itr1.next if itr1 else headB
            itr2 = itr2.next if itr2 else headA