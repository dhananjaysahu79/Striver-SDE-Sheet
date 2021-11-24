# Leetcode 2

# Remember how 6 year old kid do addition of two numbers? I used the same intution.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sm = carry = 0
        ans = ListNode()
        itr = ans

        while l1 or l2 or carry:
            sm = 0
            if l1:
                sm += l1.val
                l1 = l1.next
            if l2:
                sm += l2.val
                l2 = l2.next
            sm += carry
            carry = sm // 10
            sm = sm % 10

            node = ListNode(sm, None)
            itr.next = node
            itr = itr.next
        return ans.next