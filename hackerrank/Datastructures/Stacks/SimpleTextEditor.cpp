#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    string s;
    vector<string> history;

    for (int i = 0; i < n; i++) {
        int op;
        scanf("%d ", &op);

        if (op == 1) {
            history.push_back(s);
            string w;
            char c;
            while ((c = getchar()) != '\n' && c != EOF) {
                w += c;
            }
            s += w;
            
        }
        else if (op == 2) {
            history.push_back(s);
            int k;
            scanf("%d", &k);
            s = s.substr(0, s.length() - k);
            
        }
        else if (op == 3) {
            int k;
            scanf("%d", &k);
            printf("%c\n", s[k - 1]);
        }
        else if (op == 4) {
            s = history.back();
            history.pop_back();
            
            
        }
    }

    return 0;
}
