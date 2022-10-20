#define SLLN SinglyLinkedListNode

SinglyLinkedListNode* reverse(SinglyLinkedListNode* llist) {
    SLLN* prev = nullptr;
    SLLN* curr = llist;
    SLLN* next = nullptr;

    while(curr != nullptr){
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}