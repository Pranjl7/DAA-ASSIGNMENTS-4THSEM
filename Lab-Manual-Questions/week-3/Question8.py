# Given an unsorted array of integers, design an algorithm and
# implement a program to sort this array using selection sort. Your
# program should also find number of comparisons and number of swaps
# required.
# Input Format:
# The first line contains number of test cases, T. For each test case,
# there will be two input lines. First line contains n (the size of array).
# Second line contains space-separated integers describing array.
# Output Format:
# The output will have T number of lines.
# For each test case T, there will be three output lines. First line will give
# the sorted array.
# Second line will give total number of comparisons. Third line will give
# total number of swaps required.
# Sample 1/0 Problem II:
# Input: Output:
# 3 -21-13 1245654766 89
# 8 comparisons = 28
# -1365-2176 46 894512 swaps =7
# 10 21323446 515465767897
# 54 6534 76 78 97 46 3251 21 comparisons = 45
# 15 swaps =9
# 63 42 223 645 652 31 324 22 553 12 54 65 86 46 32512 22 31 42 46
# 54 63 65 86 223 324 325 553 645 652
# comparisons = 105
# swaps = 14


def selection_sort_with_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr, comp, swap = selection_sort_with_count(arr)

    print(*sorted_arr)
    print("comparisons =", comp)
    print("swaps =", swap)

