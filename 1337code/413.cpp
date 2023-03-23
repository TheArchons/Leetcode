#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        int total = 0;

        for (int i = 2; i < nums.size(); i++) {
            if (nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]) {
                dp[i] = dp[i - 1] + 1;
            }

            total += dp[i];
        }

        return total;
    }
};

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    freopen("413.input", "r", stdin); // For testing. Comment out for submissions

    int n; cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    Solution s;
    cout << s.numberOfArithmeticSlices(nums) << endl;

    return 0;
}