#include <iostream>
#include <string>
using namespace std;

int singleRomanConvert(char c) {
    switch (c) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return 0;
    }
}

int romanToInt(string s) {
    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i-1 < 0) {
            sum += singleRomanConvert(s[i]);
            continue;
        }
        int prevNum = singleRomanConvert(s[i-1]);
        int num = singleRomanConvert(s[i]);
        int add = num;
        for (int curr = 2; prevNum < num; curr++) {
            add -= prevNum*2;
            if (i-curr < 0) {
                break;
            }
            prevNum = singleRomanConvert(s[i-curr]);
        }
        sum += add;
    }
    return sum;
}

int main() {
    string s;
    cin >> s;
    cout << romanToInt(s) << endl;
    return 0;
}