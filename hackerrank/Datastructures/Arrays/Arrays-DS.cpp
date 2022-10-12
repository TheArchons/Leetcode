vector<int> reverseArray(vector<int> a) {
    vector<int> revA;
    for(int i = 0; i < a.size(); i++) {
        revA.push_back(a[a.size() - i - 1]);
    }

    return revA;
}