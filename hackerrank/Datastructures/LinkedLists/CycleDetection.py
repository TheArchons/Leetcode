def has_cycle(head):
    seen = set()

    while(head.next is not None):
        if id(head) in seen:
            return 1
        seen.add(id(head))
        head = head.next

    return 0