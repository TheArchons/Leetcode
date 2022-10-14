def findMergeNode(head1, head2):
    seen = set()

    while(head1 is not None and head2 is not None):
        if id(head1) == id(head2):
            return head1.data

        if id(head1) in seen:
            return head1.data
        if id(head2) in seen:
            return head2.data

        seen.add(id(head1))
        seen.add(id(head2))
        head1 = head1.next
        head2 = head2.next
    
    while (head1 is not None):
        if id(head1) in seen:
            return head1.data
        head1 = head1.next

    while (head2 is not None):
        if id(head2) in seen:
            return head2.data
        head2 = head2.next
