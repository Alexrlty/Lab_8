class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    try:
        copy_head = head
        if not copy_head.next:
            return head
        while copy_head:
            if copy_head.data == copy_head.next.data:
                copy_head.next = copy_head.next.next
            else:
                copy_head = copy_head.next
        return head
    except AttributeError:
        return head
