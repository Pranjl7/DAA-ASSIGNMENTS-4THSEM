# I Given a knapsack of maximum capacity w. N items are provided,
# each having its own value and weight. You have to Design an algorithm
# and implement it using a program to find the list of the selected items
# such that the final selected content has weight w and has maximum
# value. You can take fractions of items,i.e. the items can be broken into
# smaller pieces so that you have to carry
# only a fraction xi of item i, where 0 <xi< 1.
# Input Format:
# First input line will take number of items N which are provided.
# Second input line will contain N space-separated array containing
# weights of all N items. Third input line will contain N space-separated
# array containing values of all N items.
# Last line of the input will take the maximum capacity w of knapsack.
# Output Format:
# First output line will give maximum value that can be achieved.
# Next Line of output will give list of items selected along with their
# fraction of amount which has been taken.
# Sample 1/0O Problem II:
# Input: Output:
# 6 Maximum value : 22.33
# 6103513 item

n = int(input())
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
w = int(input())

items = []
for i in range(n):
    items.append((val[i]/wt[i], wt[i], val[i], i+1))

items.sort(reverse=True)

total = 0
res = []

for ratio, weight, value, idx in items:
    if w >= weight:
        w -= weight
        total += value
        res.append((idx, 1))
    else:
        frac = w / weight
        total += value * frac
        res.append((idx, frac))
        break

print("Maximum value :", round(total, 2))
for i, f in res:
    print("item", i, ":", round(f, 2))