# l. Given a list of activities with their starting time and finishing time.
# Your goal is to select maximum number of activities that can be
# performed by a single person such that selected activities must be nonconflicting.
# Any activity is said to be non-conflicting if starting time of an
# activity is greater than or equal to the finishing time of the other activity.
# Assume that a person can only work on a single activity at a time.
# Input Format:
# First line of input will take number of activities N.
# Second line will take N space-separated values defining starting time
# for all the N activities. Third line of input will take N space-separated
# values defining finishing time for all the N activities.
# Output Format:
# Output will be the number of non-conflicting activities and the list of
# selected activities.
# Sample 1/O Problem I:
# Input: Output:
# 10 No. of non-conflicting activities: 4
# 13053588212 List of selected activities: 1, 4, 7, 10
# 456799111214 16

n = int(input())
start = list(map(int, input().split()))
finish = list(map(int, input().split()))

activities = []
for i in range(n):
    activities.append((finish[i], start[i], i + 1))

activities.sort()

count = 0
res = []
last_end = -1

for f, s, idx in activities:
    if s >= last_end:
        res.append(idx)
        last_end = f
        count += 1

print("No. of non-conflicting activities:", count)
print("List of selected activities:", *res)