# Given an unsorted array of integers, design an algorithm and
# implement it using a program to find Kth smallest or largest element in
# the array. (Worst case Time Complexity = O(n))
# Input Format:
# The first line contains number of test cases, T. For each test case,
# there will be three input lines. First line contains n (the size of array).
# Second line contains space-separated integers describing array. Third
# line contains K.
# Output Format:
# The output will have T number of lines.
# For each test case, output will be the Kth smallest or largest array
# element. If no Kth element is present, output should be “not present”.
# Sample for Kth smallest:
# Input: Output:
# 3 123
# 10 78
# 123 656 54 765 344 514 765 34 765 234
# 3
# 15
# 4364 13 78 864 346 786 456 21 19 8 434 76 270 601
# 8


def select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    medians = [sorted(group)[len(group)//2] for group in groups]

    pivot = select(medians, len(medians)//2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return select(highs, k - len(lows) - len(pivots))


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    K = int(input())

    if K <= 0 or K > n:
        print("not present")
    else:
        result = select(arr, K - 1)
        print(result)
