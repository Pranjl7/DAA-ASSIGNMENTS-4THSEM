# Given an unsorted array of integers, design an algorithm and
# implement it using a program to sort an array of elements by
# partitioning the array into two subarrays based on a pivot element such
# that one of the sub array holds values smaller than the pivot element
# while another sub array holds values greater than the pivot element.
# Pivot element should be selected randomly from the array. Your
# program should also find number of comparisons and swaps required
# for sorting the array.
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
# Sample 1/0O Problem II:
# Input: Output:
# 3 2123324546 65 76 89
# 8 comparisons = 14
# 2365217646 894532 swaps =10
# 10 21323446515465767897
# 54 6534 76 78 97 46 32 5121 comparisons = 29
# 2023-24 and 2024-25 onwards
# 15 swaps = 21
# 63 42 223 645 652 31 324 22 553 12 54 65 86 46 32512 22 31 42 46
# 54 63 65 86 223 324 325 553 645 652
# comparisons = 45
# swaps = 39


import random

def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def partition(low, high):
        nonlocal comparisons, swaps

        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps += 1
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr, comp, swap = quick_sort(arr)

    print(*sorted_arr)
    print("comparisons =", comp)
    print("swaps =", swap)
