#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }
    unsigned int numberOfDigits = 0;
    //divide until x < 0
    int x2 = x;
    while (x2 > 0) {
        x2 /= 10;
        numberOfDigits++;
    }
    int numTotal = numberOfDigits;
    int i = 10;
    for (unsigned int a = 0; a < numTotal/2; a++) {
        int j = 1;
        for (int k = 0; k < numberOfDigits-1; k++) {
            j *= 10;
        }
        int z = 1;
        for (int k = 0; k < numTotal-numberOfDigits; k++) {
            z *= 10;
        }
        if ((x%i)/z != (x/j)%10) {
            return false;
        }
        numberOfDigits--;
        i *= 10;
    }
    return true;
}

int main() {
    int num;
    cin >> num;
    cout << isPalindrome(num);
}