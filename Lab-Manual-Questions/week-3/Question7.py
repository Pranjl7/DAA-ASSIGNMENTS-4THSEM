# // Given an unsorted array of integers, design an algorithm and a
# // program to sort the array using insertion sort. Your program should be
# // able to find number of comparisons and shifts ( shifts - total number of
# // times the array elements are shifted from their place) required for
# // sorting the array.
# // Input Format:
# // The first line contains number of test cases, T. For each test case,
# // there will be two input lines. First line contains n (the size of array).
# // Second line contains space-separated integers describing array.
# // Output Format:
# // The output will have T number of lines.
# // For each test case T, there will be three output lines. First line will give
# // the sorted array.
# // Second line will give total number of comparisons.
# // Third line will give total number of shift operations required.
# // Sample 1/O Problem I:
# // Input: Output:
# // 3 -31-23 324546 65 76 89
# // 8 comparisons = 13
# // 2023-24 and 2024-25 onwards
# // -23 65 -31 76 46 89 45 32 shifts = 20
# // 10 21323446 51546576 7897
# // 54 6534 76 78 97 46 3251 21 comparisons = 28
# // 15 shifts = 37
# // 63 42 223 645 652 31 324 22 553 -12 54 65 86 46 325 -12 22 31
# // 42 46 54 63 65 86 223 324 325 553 645 652
# // comparisons = 54
# // shifts = 68


def insertion_sort_with_count(arr):
    comparisons = 0
    shifts = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, shifts


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr, comp, shift = insertion_sort_with_count(arr)

    print(*sorted_arr)
    print("comparisons =", comp)
    print("shifts =", shift)
