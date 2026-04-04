# Il Assume that same road construction project is given to another
# 2023-24 and 2024-25 onwards
# person. The amount he will earn from this project is directly proportional
# to the budget of the project. This person is greedy, so he decided to
# maximize the budget by constructing those roads who have highest
# construction cost. Design an algorithm and implement it using a
# program to find the maximum budget required for the project.
# Input Format:
# The first line of input takes number of vertices in the graph.
# Input will be the graph in the form of adjacency matrix or adjacency list.
# Output Format:
# Out will be maximum spanning weight.
# Sample 1/0 Problem IlI:
# Input: Output:
# 7 Maximum Spanning Weight: 59
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

def max_kruskal(adj, v):
    edges = []

    for i in range(v):
        for j in range(i + 1, v):
            if adj[i][j] != 0:
                edges.append((adj[i][j], i, j))

    edges.sort(reverse=True)

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

print("Maximum Spanning Weight:", max_kruskal(adj, v))