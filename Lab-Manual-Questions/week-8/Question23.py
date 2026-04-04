# 1. Implement the previous problem using Kruskal's algorithm.
# Input Format:
# The first line of input takes number of vertices in the graph.
# Input will be the graph in the form of adjacency matrix or adjacency list.
# Output Format:
# Output will be minimum spanning weight
# Sample 1/O Problem | and II:
# Input: Output:
# 7 Minimum Spanning Weight: 39
# 0075000
# 0085000
# 7809700
# 50901560
# 05715089
# 00068011
# 00009110

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xr = find(parent, x)
    yr = find(parent, y)

    if rank[xr] < rank[yr]:
        parent[xr] = yr
    elif rank[xr] > rank[yr]:
        parent[yr] = xr
    else:
        parent[yr] = xr
        rank[xr] += 1

def kruskal(adj, v):
    edges = []

    for i in range(v):
        for j in range(i + 1, v):
            if adj[i][j] != 0:
                edges.append((adj[i][j], i, j))

    edges.sort()

    parent = [i for i in range(v)]
    rank = [0] * v

    total = 0
    count = 0

    for wt, u, w in edges:
        if find(parent, u) != find(parent, w):
            union(parent, rank, u, w)
            total += wt
            count += 1
            if count == v - 1:
                break

    return total

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

print("Minimum Spanning Weight:", kruskal(adj, v))