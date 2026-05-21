# 1. Given a long list of tasks. Each task takes specific time to
# accomplish it and each task has a deadline associated with it. You have
# to design an algorithm and implement it using a program to find
# maximum number of tasks that can be completed without crossing their
# 2023-24 and 2024-25 onwards
# deadlines and also find list of selected tasks.
# Input Format:
# First line will give total number of tasks n.
# Second line of input will give n space-separated elements of array
# representing time taken by each task.
# Third line of input will give n space-separated elements of array
# representing deadline associated with each task.
# Output Format:
# Output will be the total number of maximum tasks that can be
# completed.
# Sample 1/0 Problem II:
# Input: Output:
# 7 Max number of tasks = 4
# 2132221 Selected task numbers : 1, 2, 3, 6
# 2386253

import heapq

n = int(input())
time = list(map(int, input().split()))
deadline = list(map(int, input().split()))

tasks = []
for i in range(n):
    tasks.append((deadline[i], time[i], i + 1))

tasks.sort()

curr_time = 0
max_heap = []
selected = []

for d, t, idx in tasks:
    curr_time += t
    heapq.heappush(max_heap, (-t, idx))
    selected.append(idx)

    if curr_time > d:
        rem_t, rem_idx = heapq.heappop(max_heap)
        curr_time += rem_t
        selected.remove(rem_idx)

print("Max number of tasks =", len(selected))
print("Selected task numbers :", *selected)