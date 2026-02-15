# Given an unsorted array of integers, design an algorithm and
# implement it using a program to sort an array of elements by dividing
# the array into two subarrays and combining these subarrays after
# sorting each one of them. Your program should also find number of
# comparisons and inversions during sorting the array.
# 2 Input Format:
# " | The first line contains number of test cases, T. For each test case,
# there will be two input lines. First line contains n (the size of array).
# Second line contains space-separated integers describing array.
# Output Format:
# The output will have T number of lines.
# For each test case T, there will be three output lines. First line will give
# the sorted array.
# Second line will give total number of comparisons. Third line will give
# 2023-24 and 2024-25 onwards
# total number of inversions required.
# Sample 1/O Problem I:
# Input: Output:
# 3 2123324546 6576 89
# 8 comparisons = 16
# 2365217646 894532 inversions =
# 10 213234465154 65767897
# 54 6534 76 78 97 46 32 51 21 comparisons = 22
# 15 inversions =
# 63 42 223 645 652 31 324 22 553 12 54 65 86 46 32512 22 31 42 46
# 54 63 65 86 223 324 325 553 645 652
# comparisons = 43
# inversions =


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0, 0

    mid = len(arr) // 2
    left, comp_left, inv_left = merge_sort(arr[:mid])
    right, comp_right, inv_right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    comparisons = comp_left + comp_right
    inversions = inv_left + inv_right

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += (len(left) - i)
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, comparisons, inversions


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr, comp, inv = merge_sort(arr)

    print(*sorted_arr)
    print("comparisons =", comp)
    print("inversions =", inv)
