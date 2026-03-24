def loop_size(node):
    slow = node
    fast = node
    lenght = 0
    while node:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = node
            while node:
                slow = slow.next
                fast = fast.next
                if slow == fast:
                    start = slow
                    while node:
                        fast = fast.next
                        lenght += 1
                        if fast == start:
                            return lenght
