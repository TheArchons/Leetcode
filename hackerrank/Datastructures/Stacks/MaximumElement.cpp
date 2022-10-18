#include <vector>
#include <stdio.h>
#include <set>

vector<int> getMax(vector<string> operations) {
    vector<int> stack;
    vector<int> results;
    multiset<int> maxes;
    int operation_count = operations.size();

    for (int i = 0; i < operation_count; i++) {
        string operation = operations[i];
        if (operation[0] == '1') {
            int number = stoi(operation.substr(2));
            stack.push_back(number);
            maxes.insert(number);
        } else if (operation[0] == '2') {
            maxes.erase(maxes.find(stack.back()));
            stack.pop_back();
        } else if (operation[0] == '3') {
            results.push_back(*maxes.rbegin());
        }
    }

    return results;
}