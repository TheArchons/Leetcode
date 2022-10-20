void reversePrint(SinglyLinkedListNode* llist) {
    vector<int> list;

    while(llist != nullptr){
        list.push_back(llist->data);
        llist = llist->next;
    }

    for(int i = list.size() - 1; i >= 0; i--){
        printf("%d\n", list[i]);
    }
}
