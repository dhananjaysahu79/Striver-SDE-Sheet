class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int):
        self.head, self.length, self.k = head, 0, k
        
        def traverse(node):
            if not node: return node
            self.length += 1
            right = traverse(node.next)
            if right == None: 
                self.k = self.k % self.length
                right = node
            if self.k == 0:
                right.next = self.head
                right = node.next
                node.next = None
            self.k -= 1
            return right or node
        return traverse(head)