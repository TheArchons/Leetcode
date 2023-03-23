#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int prev, maxVal;
        prev = maxVal = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            int curr = max(prev + nums[i], nums[i]);
            maxVal = max(maxVal, curr);
            prev = curr;
        }

        return maxVal;
    }
};

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    freopen("53.input", "r", stdin); // For testing. Comment out for submissions

    int n; cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    Solution s;
    cout << s.maxSubArray(nums) << endl;

    return 0;
}