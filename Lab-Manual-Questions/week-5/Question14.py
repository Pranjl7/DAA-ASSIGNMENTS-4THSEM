# Given an unsorted array of integers, design an algorithm and
# implement it using a program to find whether two elements exist such
# that their sum is equal to the given key element. (Time Complexity =
# O(n log n))
# Input Format:
# The first line contains number of test cases, T. For each test case,
# there will be two input lines. First line contains n (the size of array).
# Second line contains space-separated integers describing array. Third
# line contains key
# 2023-24 and 2024-25 onwards
# Output Format:
# The output will have T number of lines.
# For each test case, output will be the elements arr|i] and arr{j] such that
# arr[i]+arr[j] = key if exist otherwise print '‘No Such Elements Exist”.
# Sample 1/O Problem II:
# Input: Output:
# 2 10 40
# 10 No Such Element Exist
# 64 28 97 40 1272 84 24 38 10
# 50
# 15
# 56 10729129341456120113991294
# 302


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())

    arr.sort()

    left = 0
    right = n - 1
    found = False

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == key:
            print(arr[left], arr[right])
            found = True
            break
        elif current_sum < key:
            left += 1
        else:
            right -= 1

    if not found:
        print("No Such Elements Exist")
