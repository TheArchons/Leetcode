#include <iostream>
#include <string>
#include <vector>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    string output = "";
    if (strs.size() == 0) {
        return "";
    }
    if (strs.size() == 1) {
        return strs[0];
    }
    for (int i = 0; i < strs[0].length(); i++) {
        for (int j = 1; j < strs.size(); j++) {
            if (strs[j][i] != strs[0][i]) {
                return output;
            }
        }
        output += strs[0][i];
    }
    return output;
}

int main() {
    int len;
    cin >> len;
    vector<string> strs(len);
    for (int i = 0; i < len; i++) {
        cin >> strs[i];
    }
    cout << longestCommonPrefix(strs) << endl;
}