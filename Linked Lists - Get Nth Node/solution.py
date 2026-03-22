from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def lenght(node):
    num = 0
    while node:
        node = node.next
        num += 1
    return num

def get_nth(node, index):
    if not (0 <= index <= lenght(node)-1):
        raise ValueError
    for i in range(index):
        node = node.next
    return node
    
  
