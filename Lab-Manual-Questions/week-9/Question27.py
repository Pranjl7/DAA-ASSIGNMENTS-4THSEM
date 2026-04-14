# 1. Given an array of elements. Assume arrfi] represents the size of
# file i. Write an algorithm and a program to merge all these files into
# single file with minimum computation. For given two files A and B with
# sizes m and n, computation cost of merging them is O(m+n). (Hint: use
# greedy approach)
# Input Format:
# First line will take the size n of the array. Second line will take array s
# an input.
# Output Format:
# Output will be the minimum computation cost required to merge all the
# elements of the array.
# Sample 1/O Problem IlI:
# 2023-24 and 2024-25 onwards
# Input: Output:
# 10 960
# 10 5100 50 20 15 520 100 10

import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

cost = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    s = a + b
    cost += s
    heapq.heappush(arr, s)

print(cost)