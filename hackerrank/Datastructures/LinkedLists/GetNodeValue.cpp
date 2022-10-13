#define SLLN SinglyLinkedListNode

int getNode(SinglyLinkedListNode* llist, int positionFromTail) {
    SLLN* offset = llist;
    while(llist != NULL) {
        if(positionFromTail == -1) {
            offset = offset->next;
        }
        else {
            positionFromTail--;
        }
        llist = llist->next;
    }
    return offset->data;
}