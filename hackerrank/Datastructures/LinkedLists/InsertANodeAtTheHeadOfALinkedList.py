def insertNodeAtHead(llist, data):
    startNode = SinglyLinkedListNode(data)
    if llist is not None:
        startNode.next = llist
    
    return startNode