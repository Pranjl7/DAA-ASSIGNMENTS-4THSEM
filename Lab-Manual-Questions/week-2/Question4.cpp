// Given a sorted array of positive integers containing few duplicate
// elements, design an algorithm and implement it using a program to find
// whether the given key element is present in the array or not. If present,
// then also find the number of copies of given key. (Time Complexity =
// O(log n))
// Input format:
// The first line contains number of test cases, T. For each test case,
// there will be three input lines. First line contains n (the size of array).
// 2. | Second line contains space-separated integers describing array.
// Third line contains the key element that need to be searched in the
// array.
// Output format:
// The output will have T number of lines.
// For each test case T, output will be the key element and its number of
// copies in the array if the key element is present in the array otherwise
// print “ Key not present”.
// Sample 1/O Problem I:
// Input: Output:
// 2023-24 and 2024-25 onwards
// 2 981-2
// 10 75-3
// 235 235 278 278 763 764 790 853 981 981
// 981
// 15
// 1223355525757575979 977
// 75

#include <iostream>
using namespace std;

int firstOccurrence(int arr[], int n, int key) {
    int low = 0, high = n - 1, ans = -1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == key) {
            ans = mid;
            high = mid - 1;
        }
        else if (key < arr[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return ans;
}

int lastOccurrence(int arr[], int n, int key) {
    int low = 0, high = n - 1, ans = -1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == key) {
            ans = mid;
            low = mid + 1;
        }
        else if (key < arr[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return ans;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        int key;
        cin >> key;

        int first = firstOccurrence(arr, n, key);

        if (first == -1) {
            cout << "Key not present\n";
        } else {
            int last = lastOccurrence(arr, n, key);
            cout << key << " " << (last - first + 1) << "\n";
        }
    }
    return 0;
}
