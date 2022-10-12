def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)
    head = llist

    for i in range(position-1):
        head = head.next
    
    next = head.next

    head.next = node
    node.next = next

    return llist