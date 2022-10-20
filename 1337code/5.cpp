#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

bool palidrome(string s) {
    string sR = s;
    reverse(sR.begin(), sR.end());
    return s == sR;
}

string longestPalindrome(string s) {
    int sLen = s.length();
    for(int strLen = sLen; strLen > 0; strLen--) {
        for(int i = 0; i < sLen - strLen + 1; i++) {
            if(s[i] == s[strLen+i-1]) {
                string sSub = s.substr(i, strLen);
                if (palidrome(sSub)) {
                    return sSub;
                }
            }

        }
    }
    return "";
}

int main() {
    string input;
    cin >> input;
    cout << longestPalindrome(input);
}