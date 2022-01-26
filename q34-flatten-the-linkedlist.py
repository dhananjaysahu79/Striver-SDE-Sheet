# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next

def merge(head1,head2):
    head = itr = None
    while head1 and head2:
        temp = head2
        if head1.data < head2.data: 
            temp = head1
            head1 = head1.child
        else: head2 = head2.child
        
        if head == None:
            head = itr = temp
        else: 
            itr.child = temp
            itr = itr.child
    if head1: 
        if head == None:
            itr = head = head1
        else:
            itr.child = head1
            itr = itr.child
    if head2: 
        if head == None:
            itr = head = head2
        else:
            itr.child = head2
            itr = itr.child
    return head
           
            
        

def flattenLinkedList(head):
    if not head: return head
    head1 = flattenLinkedList(head.next)
    return merge(head, head1)
    
    