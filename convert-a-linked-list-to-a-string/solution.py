def stringify(node):
    result = []
    while node is not None:
        result.append(str(node.data))
        node = node.next
    result.append('None')
    return " -> ".join(result)
