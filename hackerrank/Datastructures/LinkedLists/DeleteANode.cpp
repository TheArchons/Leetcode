#define SLLN SinglyLinkedListNode

SinglyLinkedListNode* deleteNode(SinglyLinkedListNode* llist, int position) {
    SLLN* start = llist;
    if (position == 0) {
        return llist->next;
    }
    for (int i = 0; i < position-1; i++) {
        llist = llist->next;
    }

    llist->next = llist->next->next;
    return start;
}