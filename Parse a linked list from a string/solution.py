from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    list_of_pure = list_repr.split(' -> ')[:-1]
    head = None
    for data in list_of_pure[::-1]:
        head = Node(int(data), head)
    return head
        
