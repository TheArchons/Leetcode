#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m > n) {
            int temp = m;
            m = n;
            n = temp;
        }

        vector<vector<int>> dp(2, vector<int>(m, 1));

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                dp[1][j] = dp[0][j] + dp[1][j - 1];
            }

            dp[0] = dp[1];
        }

        return dp[1][m - 1];
    }
};

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    freopen("62.input", "r", stdin); // For testing. Comment out for submissions

    int m; cin >> m; int n; cin >> n;

    Solution s;
    cout << s.uniquePaths(m, n) << endl;

    return 0;
}