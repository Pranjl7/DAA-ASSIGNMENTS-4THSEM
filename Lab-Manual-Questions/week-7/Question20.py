# Design an algorithm and implement it using a program to solve
# previous question's problem using Bellman- Ford's shortest path
# algorithm.
# Input Format:
# Input will be the graph in the form of adjacency matrix or adjacency list.
# Source vertex number is also provided as an input.
# Output Format:
# Output will contain V lines.
# Each line will represent the whole path from destination vertex number
# to source vertex number along with minimum path weigth.
# Sample 1/O Prob|l aned mII:
# Input: Output:
# 5 1:0
# 04100 231:3
# 00004 31:1
# 02040 431:3
# 00004 5231:7
# 00000

def bellman_ford(adj, v, src):
    dist = [float('inf')] * v
    parent = [-1] * v
    dist[src] = 0

    edges = []
    for i in range(v):
        for j in range(v):
            if adj[i][j] != 0:
                edges.append((i, j, adj[i][j]))

    for _ in range(v - 1):
        for u, w, wt in edges:
            if dist[u] != float('inf') and dist[w] > dist[u] + wt:
                dist[w] = dist[u] + wt
                parent[w] = u

    return dist, parent

def path(parent, j):
    p = []
    while j != -1:
        p.append(j + 1)
        j = parent[j]
    return p

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

src = int(input()) - 1

dist, parent = bellman_ford(adj, v, src)

for i in range(v):
    p = path(parent, i)
    print(*p, sep="", end=":")
    print(dist[i])