class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise VallueError
    if not head.next.next:
        first_head = head
        second_head = head.next
        return Context(Node(first_head.data), Node(second_head.data))
    h1 = head
    h2 = head.next
    first_head = head
    second_head = head.next
    while second_head:
        first_head.next = second_head.next
        first_head = second_head
        second_head = first_head.next
    first_head.next = None
    return Context(h1, h2)
