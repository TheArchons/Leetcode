#include <iostream>
#include <string>
using namespace std;

string convert(string s, int numRows) {
    if (numRows == 1) return s;
    int skipLen = (numRows * 2) - 2, startPos;
    startPos = 0;
    string result = "";
    while(skipLen > 0) {
        bool isLong = true;
        result += s[startPos];
        for(int i = startPos + skipLen; i < s.length(); i += 0) {
            if (startPos == 0) {
                isLong = true;
            }
            if (isLong) {
                i += skipLen;
                result += s[i];
                isLong = false;
            }
            else {
                i += startPos*2;
                result += s[i];
                isLong = true;
            }
        }
        startPos++;
        skipLen -= 2;
    }
    int finalLine = numRows-1;
    for(int i = finalLine; i < s.length(); i += (finalLine*2)) {
        result += s[i];
    }
    return result;
}

int main() {
    string input;
    int numRows;
    cin >> input >> numRows;
    cout << convert(input, numRows);
}