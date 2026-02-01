// Given a sorted array of positive integers, design an algorithm
// and implement it using a program to find three indices i, j, k such that
// arrli] + arr[j] = arr[k].
// Input format:
// The first line contains number of test cases, T. For each test case,
// there will be two input lines. First line contains n (the size of array).
// Second line contains space-separated integers describing array.
// Output:
// The output will have T number of lines.
// For each test case T, print the value of i, j and k, if found else print “No
// sequence found”.
// Sample 1/0O Problem II:
// Input: Output:
// 3 No sequence found.
// 5 2,7,8
// 1584209 341 1,6,9
// 10
// 2428 48 71 86 89 92 120 194 201
// 15
// 64 69 82 95 99 107 113 141 171 350 369 400 511 590 666

#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        bool found = false;

        for (int k = n - 1; k >= 2 && !found; k--) {
            int i = 0, j = k - 1;

            while (i < j) {
                int sum = arr[i] + arr[j];

                if (sum == arr[k]) {
                    cout << i + 1 << " " << j + 1 << " " << k + 1 << "\n";
                    found = true;
                    break;
                }
                else if (sum < arr[k]) {
                    i++;
                }
                else {
                    j--;
                }
            }
        }

        if (!found)
            cout << "No sequence found\n";
    }

    return 0;
}
