#define SLLN SinglyLinkedListNode

SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    SLLN* prev = NULL;
    SLLN* start = head1;
    while(head1 != NULL) {
        if(head2 == NULL) break;
        if(head1->data > head2->data) {
            if (prev == NULL) {
                start = head2;
                prev = head2;
                head2 = head2->next;
                prev->next = head1;
            }
            else {
                prev->next = head2;
                prev = head2;
                head2 = head2->next;
                prev->next = head1;
            }
        }
        else {
            prev = head1;
            head1 = head1->next;
        }
    }
    if(head2 != NULL) {
        prev->next = head2;
    }
    return start;
}