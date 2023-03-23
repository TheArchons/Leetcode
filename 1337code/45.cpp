#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, INT_MAX);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= nums[i]; j++) {
                int jumpPos = i + j;

                if (jumpPos < n) {
                    dp[jumpPos] = min(dp[jumpPos], dp[i] + 1);
                }
            }
        }

        return dp[n - 1];
    }
};

int main() {
    int n; cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    Solution s;
    cout << s.jump(nums) << endl;
}