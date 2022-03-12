solution = "https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1842854/Python-Very-Easy-Solutions-or-Explained-or-O(1)-space"

# Solution: 1 Hashing
# Space: O(N)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic, itr = {}, head                                   # dic: to store each original node pointing to its copy node, itr: iterator to travese the original list
        copy_head = prev = Node(-1)                           # copy_head: head of copy List (not exactly head, but head will be at next to it), prev: this will point to previous node of Copy list, used for linking the next
        
        while itr:                                            # traverse the Original list and make the copy, we will leave the random to None as of now
            prev.next = prev = dic[itr] = Node(x = itr.val)   # make a New node with original value, link the prev.next to new node, then update the prev pointer to this new Node
            itr = itr.next                                    # update the itr to next, so we can move to the next node of original list

        copy_itr, itr = copy_head.next, head                  # copy_itr: iterator to traverse the copy list, itr: to traverse the original list
        while itr:                                            # since both are of same length, we can take while itr or while copy_itr as well
            if itr.random: copy_itr.random = dic[itr.random]  # if original has random pointer(ie not None) then update the random of copy node. Every original node is pointing to copy node in our dictionary, we will get the copy Node.
            itr, copy_itr  = itr.next, copy_itr.next          # update both iterator to its next in order to move further.
        return copy_head.next    

# Solution: 2
# Space: O(1)


#             (1st Copy)                       (2nd Copy)                      (3rd Copy)
#        ---->   | 1 | next | random |    ---> | val | next | random |    ---> | 3 | next | random |                                              
#        |	           |__________      |             |___________      |       
# 	   | 	                      |     |                         |     |      
# | 1 | next | random |           | 2 | next | random |            | 3 | next | random |        <---- Original List
#                 |__________________________________________________|
					
# 1. In one loop We traversed and added the copy in between the original nodes.
# 2. In second loop with will get the random, How?
#    -> In above Example, 1st Node's random is 3rd Node.
#       So, 1st Copy 's random will be the next node of 3rd Node (1st -> random -> next)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        itr = head                                         # itr: iterator to iterate the original
        while itr:                                         # iterate the original list
            itr.next = Node(x = itr.val, next = itr.next)  # create the copy node (with original node's value and original node's next so as chain would not break) and add this to original.next (ie. adding a copy in between the two original nodes) 
            itr = itr.next.next                            # since we have added a copy in between, so have to skip that to get next original node
        copy_head = prev = Node(-1)                        # copy_head: head of copy List (not exactly head, but head will be at next to it), prev: this will point to previous node of Copy list, used for linking the next
        itr = head                                         # itr: we will iterate again from head
        while itr:
            prev.next = prev = itr.next                    # each orginal node's next will have the copy Node, point prev to it , and update the prev to itr.next as well
            if itr.random: prev.random = itr.random.next   # if any original node has random, we can go to the random node and grab its next bcoz we know any original node's next is their copy node.
            itr = itr.next.next                            # again we have skip the copy to get the next original node
        return copy_head.next