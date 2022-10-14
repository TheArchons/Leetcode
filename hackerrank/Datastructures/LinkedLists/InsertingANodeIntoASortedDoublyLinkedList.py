def sortedInsert(llist, data):
    start = llist
    node = DoublyLinkedListNode(data)
    if llist.data > data:
        node.next = llist
        llist.prev = node
        return node

    while (llist.next is not None and llist.next.data < data):
        llist = llist.next
    
    next = llist.next
    llist.next = node
    node.prev = llist
    node.next = next
    if next is not None:
        next.prev = node
    
    return start