# You have been given two sorted integer arrays of size m and n.
# Design an algorithm and implement it using a program to find list of
# elements which are common to both. (Time Complexity = O(m+n))
# Input Format:
# First line contains m (the size of first array).
# Second line contains m space-separated integers describing first array.
# Third line contains n (the size of second array).
# Fourth line contains n space-separated integers describing second
# array.
# Output Format:
# Output will be the list of elements which are common to both.
# Sample 1/0O Problem IlI:
# 2023-24 and 2024-25 onwards
# Input: Output:
# 7 10 10 34 55
# 3476 1039851055
# 12
# 305534721034 1089 11 30 69 51


m = int(input())
arr1 = list(map(int, input().split()))

n = int(input())
arr2 = list(map(int, input().split()))

i = 0
j = 0
common = []

while i < m and j < n:
    if arr1[i] == arr2[j]:
        common.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1

if common:
    print(*common)
else:
    print("No Common Elements")
