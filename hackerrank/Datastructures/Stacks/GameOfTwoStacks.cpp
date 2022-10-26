#include <vector>
#include <algorithm>

int twoStacks(int maxSum, vector<int> a, vector<int> b) {
    long long int sum; int count; int maxCount;
    count = sum = maxCount = 0;

    for (int i = 0; i < a.size(); i++) {
        sum += a[i];
        if (sum > maxSum) {
            sum -= a[i];
            break;
        }
        count++;
    }

    maxCount = count;
    int lCount = count;

    for (int i = 0; i < b.size() && lCount > 0; i++) {
        sum += b[i];
        count++;
        while (sum > maxSum) {
            sum -= a[lCount];
            lCount--;
            count--;
        }
        if (count > maxCount) {
            maxCount = count;
        }
    }

    return maxCount;
}