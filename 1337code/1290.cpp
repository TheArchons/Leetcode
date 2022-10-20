int getDecimalValue(ListNode* head) {
    ListNode *l = head;
    string binaryStr = "";
    while (l->next != nullptr) {
        binaryStr += to_string(l->val);
        l = l -> next;
    }
    binaryStr += to_string(l->val);
    return stol(binaryStr,nullptr,2);
}