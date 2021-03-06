#include <iostream>
#include <string>
using namespace std;

string convert(string s, int numRows) {
    if (numRows == 1) return s;
    int height = numRows;
    numRows += numRows - 2;
    string out = "";
    for(int difference = 0, layer = 0; layer < height; layer++, difference += 2) {
        int currentPos = layer;
        bool isLong = true;
        int add = 0;
        if (layer == numRows-2) {
            difference = numRows;
        }
        while (currentPos < s.length()) {
            out += s[currentPos];
            if (isLong) {
                if (numRows - difference <= 0) {
                    add = 0;
                }
                else {
                    add = difference;
                }
                currentPos += numRows - add;
            } else {
                if (difference == 0 || difference >= numRows) {
                    add = numRows;
                }
                else {
                    add = difference;
                }
                currentPos += add;
            }
            isLong = !isLong;
        }
    }
    return out;
}

int main() {
    string input;
    int numRows;
    cin >> input >> numRows;
    cout << convert(input, numRows);
}