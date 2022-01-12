#include<stdio.h>
using namespace std;

ListNode* reverseList(ListNode* head) {
    if (head == nullptr) {
        return head;
    }
    ListNode* curr = head;
    ListNode *next, *prev;
    prev = nullptr;
    while (curr != nullptr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}