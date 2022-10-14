def removeDuplicates(llist):
    start = llist
    tail = llist
    while llist.next is not None:
        tail = llist
        while llist.data == tail.data and llist.next is not None:
            llist = llist.next
        if tail.data == llist.data:
            tail.next = None
        else:
            tail.next = llist

    return start
