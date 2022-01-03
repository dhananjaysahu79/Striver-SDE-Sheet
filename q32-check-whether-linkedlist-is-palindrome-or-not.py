# Solution 1 (Naive Approach) :
# Just extract all the list values into an array.
# Then use two pointers approach to check the palidrome.
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        itr = head
        
        while itr:
            arr.append(itr.val)
            itr = itr.next
        
        a = 0; b = len(arr) - 1
        
        while a <= b:
            if arr[a] != arr[b]: return False
            a += 1
            b -= 1
        return True
        
# Solution 2 :
# Find the middle node and then reverse the nodes after that, then use the two pointer technique to check the list is palindrome or not.
# Time Complexity: O(N)
# Space Complexity: O(1)
# However this will lead to more runtime

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def findMiddle(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.next if fast else slow
        
        def reverse(mid):
            itr = prev = mid
            while itr:
                temp = itr.next
                if itr == mid: itr.next = None
                else: itr.next = prev
                prev = itr
                itr = temp
            return prev
            
        
        mid = findMiddle(head)
        end = reverse(mid)
        
        while end and head:
            if end.val != head.val: return False
            end = end.next
            head = head.next
        return True