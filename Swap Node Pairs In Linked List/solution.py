from preloaded import Node
def swap_pairs(head):
    if not head or not head.next:
        return head
    head_1 = head
    head_2 = head.next
    head_1.next = head_2.next
    head_2.next = head_1
    new_head = head_2
    prev = head_1
    current = head_1.next
    while current and current.next:
        head_1 = current
        head_2 = current.next
        head_1.next = head_2.next
        head_2.next = head_1
        prev.next = head_2
        prev = head_1
        current = head_1.next
    return new_head
