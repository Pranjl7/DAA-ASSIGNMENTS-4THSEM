# l. Given a (directed/undirected) graph, design an algorithm and
# implement it using a program to find if a path exists between two given
# vertices or not. (Hint: use DFS)
# Input Format:
# Input will be the graph in the form of adjacency matrix or adjacency list.
# Source vertex number and destination vertex number is also provided
# as an input.
# Output Format:
# Output will be 'Yes Path Exists' if path exists, otherwise print 'No Such
# 2023-24 and 2024-25 onwards
# Path Exists'. Sample 1/O Problem I

def dfs(adj, visited, u, dest):
    if u == dest:
        return True
    visited[u] = True
    for v in range(len(adj)):
        if adj[u][v] != 0 and not visited[v]:
            if dfs(adj, visited, v, dest):
                return True
    return False

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

src = int(input())
dest = int(input())

visited = [False] * v

if dfs(adj, visited, src, dest):
    print("Yes Path Exists")
else:
    print("No Such Path Exists")