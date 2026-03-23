""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def sorted_insert(head, data):
    if not head or data < head.data:
        return Node(data, head)
    else:
        head.next = sorted_insert(head.next, data)
        return head
