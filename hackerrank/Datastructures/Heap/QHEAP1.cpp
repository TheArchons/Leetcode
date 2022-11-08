#include <iostream>
#include <set>

using namespace std;

int main() {
    int queries;
    cin >> queries;

    multiset<int> heap;

    for (int i = 0; i < queries; i++) {
        int type; int val;
        cin >> type;

        if (type == 1) {
            cin >> val;
            heap.insert(val);
        }
        if (type == 2) {
            cin >> val;
            heap.erase(heap.find(val));
        }
        if (type == 3) {
            cout << *heap.begin() << endl;
        }
    }
}