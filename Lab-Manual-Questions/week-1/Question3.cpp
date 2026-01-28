// Given an already sorted array of positive integers, design an
// algorithm and implement it using a program to find whether a given key
// element is present in the sorted array or not. For an array arr[n], search
// at the indexes arr[0], arr[2], arr[4],. ,arr[2k] and so on. Once the interval
// (arr[2k] <
// key < arr[ 2k+1] ) is found, perform a linear search operation from the
// index 2k to find the element key. (Complexity < O(n), where n is the
// number of elements need to be scanned for searching): Jump Search
// Input format:
// The first line contains number of test cases, T. For each test case,
// there will be three input lines. First line contains n (the size of array).
// Second line contains n space-separated integers describing array.
// Third line contains the key element that need to be searched in the
// array.
// Output format:
// The output will have T number of lines.
// 2023-24 and 2024-25 onwards
// For each test case, output will be “Present” if the key element is found
// in the array, otherwise “Not Present”.
// Also for each test case output the number of comparisons required to
// search the key.

// Sample 1/O Problem - 2, 3:
// Input: Output:
// 3 Present 3
// 5 Not Present 4
// 122336 39 41 Present 3
// 41
// 8
// 213940455154 6872
// 69
// 10
// 101 246 438 561 796 896 899 4644 7999 8545
// 7999


#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        int key;
        cin >> key;

        int comparisons = 0;
        int step = sqrt(n);
        int prev = 0;
        bool found = false;

        while (prev < n && arr[min(step, n) - 1] < key) {
            comparisons++;
            prev = step;
            step += sqrt(n);

            if (prev >= n)
                break;
        }

        for (int i = prev; i < min(step, n); i++) {
            comparisons++;
            if (arr[i] == key) {
                found = true;
                break;
            }
        }

        if (found)
            cout << "Present " << comparisons << endl;
        else
            cout << "Not Present " << comparisons << endl;
    }

    return 0;
}
