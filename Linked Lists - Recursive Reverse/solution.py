class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head or not head.next: # search for None / new_head
        return head
    new_head = reverse(head.next) # finds last element(new_head)
    
    head.next.next = head #  |--> changes next link to current one (2,3)-(3,None) --> (2,None)-(3,2)
    head.next = None      #  |

    return new_head # saves new head untill the end
