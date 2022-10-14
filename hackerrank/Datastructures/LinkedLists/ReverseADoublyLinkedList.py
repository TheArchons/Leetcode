def reverse(list):
    prev = None
    next = list.next
    while list is not None:
        list.next = prev
        list.prev = next
        prev = list
        list = next
        if next is not None:
            next = next.next
    
    return prev