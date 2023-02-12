#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n + 1, 0);

        dp[0] = 1;

        for (int i = 0; i <= n; i++) {
            if (i + 1 <= n) {
                dp[i + 1] += dp[i];
            }
            
            if (i + 2 <= n) {
                dp[i + 2] += dp[i];
            }
        }
        return dp[n];
    }
};

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    freopen("70.input", "r", stdin);

    int n; cin >> n;

    cout << Solution().climbStairs(n) << endl;

    return 0;
}