# Soultion breakdown:

# Find the length of the linkedlist.
# Find the number of groups that can be formed each of length k
# loop through the number of groups and reverse each of the groups using two pointers, also keep the record of tail of the current group in prev_tail so that we can point next group's head into it to form the list.
# After that when we processed all the groups, we need to link the remaining that couldn't able to form any group. We can simply add the remainings to curr_group_tail's next if any.
# Hope I am able to explain my solution. Feel free to ask any doubts.

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
    def length(itr):
        c = 0
        while itr: c += 1; itr = itr.next
        return c
    
    def reverse(itr,k):
        curr_tail, prev = itr, None
        for _ in range(k):
            temp = itr.next
            itr.next = prev
            prev = itr
            itr = temp
        return itr,prev,curr_tail
        
    
    groups = length(head) // k
    itr, ans_head = head, None
    prev_tail = curr_group_tail = None
    
    for i in range(groups):
        itr,curr_group_head, curr_group_tail = reverse(itr,k)
        if prev_tail: prev_tail.next = curr_group_head
        else: ans_head = curr_group_head
        prev_tail = curr_group_tail
        
    if curr_group_tail: curr_group_tail.next = itr
    return ans_head