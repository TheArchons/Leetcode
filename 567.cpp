#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

bool checkInclusion(string s1, string s2) {
    unordered_map<char, int> c1Counts, c1CountsClone;
    int max, curr;
    max = curr = 0;
    for (char c : s1) {
        c1Counts[c]++;
    }
    c1CountsClone = c1Counts;
    for (int i = 0; i < s2.size(); i++) {
        char c = s2[i];
        if (c1Counts[c] > 0) {
            curr++;
            if (curr > max) {
                max = curr;
            }
            c1Counts[c]--;
        }
        else {
            curr = 0;
            c1Counts = c1CountsClone;
        }
    }
    for (int i = 0; i < s1.size(); i++) {
        char c = s2[i];
        if (c1Counts[c] > 0) {
            curr++;
            if (curr > max) {
                max = curr;
            }
            c1Counts[c]--;
        }
        else {
            curr = 0;
            c1Counts = c1CountsClone;
        }
    }
    if (max == s1.size()) {
        return true;
    }
    return false;
}

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    printf(checkInclusion(s1, s2) ? "true" : "false");
}