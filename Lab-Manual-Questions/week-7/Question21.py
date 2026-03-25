# Il Given a directed graph with two vertices ( source and
# destination). Design an algorithm and implement it using a program to
# find the weight of the shortest path from source to destination with
# exactly k edges on the path.
# Input Format:
# First input line will obtain number of vertices V present in the graph.
# Graph in the form of adjacency matrix or adjacency list is taken as an
# input in next V lines.
# Next input line will obtain source and destination vertex number. Last
# input line will obtain value k.
# Output Format:
# Output will be the weigth of shortest path from source to destination
# having exactly k edges. If no path is available then print “no path of
# length k is available”.
# 2023-24 and 2024-25 onwards
# Sample 1/O Problem IlI:
# Input: Output:
# 4 Weight of shortest path from (1,4) with 2 edges : 9
# 01032
# 0007
# 0006
# 0000
# 14
# 2

def shortest_path_k_edges(adj, v, src, dest, k):
    dp = [[float('inf')] * v for _ in range(k + 1)]
    dp[0][src] = 0

    for e in range(1, k + 1):
        for i in range(v):
            for j in range(v):
                if adj[j][i] != 0 and dp[e - 1][j] != float('inf'):
                    dp[e][i] = min(dp[e][i], dp[e - 1][j] + adj[j][i])

    return dp[k][dest]

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

s, d = map(int, input())
k = int(input())

s -= 1
d -= 1

res = shortest_path_k_edges(adj, v, s, d, k)

if res == float('inf'):
    print("no path of length k is available")
else:
    print("Weight of shortest path from (", s + 1, ",", d + 1, ") with", k, "edges :", res)