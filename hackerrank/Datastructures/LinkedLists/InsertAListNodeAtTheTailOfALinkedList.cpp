#include <bits/stdc++.h>

SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) {
    SinglyLinkedListNode* start = head;
    SinglyLinkedListNode* newNode = new SinglyLinkedListNode(data);

    if (head == nullptr) {
        return newNode;
    }

    while(head->next != nullptr){
        cout << head->data << endl;
        head = head->next;
    }
    head->next = newNode;

    return start;
}