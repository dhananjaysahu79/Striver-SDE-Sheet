# Leetcode 237
# Copy the next node value and next so that the given node is skipped.
# Edge case is tail node: It is given in the question that, node will not be a tail node.

class Solution:
    def deleteNode(self, node):

        node.val, node.next = node.next.val, node.next.next