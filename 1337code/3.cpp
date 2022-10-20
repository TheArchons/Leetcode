#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> dupes;
    int sLen = s.length(), maxSize, size, backPos;
    size = maxSize = backPos = 0;
    for (int i = 0; i < sLen; i++) {
        if (size > maxSize) {
            maxSize = size;
        }
        if (dupes.find(s[i]) != dupes.end()) {
            for(int j = backPos; j < dupes[s[i]] - 1; j++) {
                dupes.erase(s[j]);
            }
            size -= dupes[s[i]]-backPos;
            size++;
            backPos = dupes[s[i]];
            dupes[s[i]] = i + 1;
        }
        else{
            dupes.insert({s[i], i+1});
            size++;
            if (size > maxSize) {
                maxSize = size;
            }
        }
    }
    return maxSize;
}

int main(string s) {
    string input;
    cin >> input;
    cout << lengthOfLongestSubstring(input);
}