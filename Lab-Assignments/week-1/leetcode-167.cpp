// LeetCode 167 – Two Sum II (Sorted Array)

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    int target;
    cin >> target;

    int left = 0, right = n - 1;

    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            cout << left + 1 << " " << right + 1;
            return 0;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return 0;
}
