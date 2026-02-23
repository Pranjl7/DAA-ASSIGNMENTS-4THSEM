# Given an unsorted array of alphabets containing duplicate
# elements. Design an algorithm and implement it using a program to find
# 5. | which alphabet has maximum number of occurrences and
# print it. (Time Complexity = O(n)) (Hint: Use counting sort)
# Input Format:
# 2023-24 and 2024-25 onwards
# The first line contains number of test cases, T. For each test case,
# there will be two input lines. First line contains n (the size of array).
# Second line contains space-separated integers describing array.
# Output:
# The output will have T number of lines.
# For each test case, output will be the array element which has
# maximum occurrences and its total number of occurrences.
# If no duplicates are present (i.e. all the elements occur only once),
# output should be “No Duplicates Present”.
# Sample 1/O Problem I:
# Input: Output:
# 3 a-3
# 10 No Duplicates Present
# aedwadqgafp 1-4
# 15
# rkpgvyumagadjcze
# 20
# gtllitcwawglcwdsaavcl


T = int(input())

for _ in range(T):
    n = int(input())
    arr = input().strip()

    count = [0] * 26
    
    for ch in arr:
        index = ord(ch) - ord('a')
        count[index] += 1
    
    max_count = max(count)
    
    if max_count == 1:
        print("No Duplicates Present")
    else:
        max_index = count.index(max_count)
        max_char = chr(max_index + ord('a'))
        print(f"{max_char}-{max_count}")
