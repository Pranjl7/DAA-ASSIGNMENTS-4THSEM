# . Given a directed graph, design an algorithm and implement it
# using a program to find whether cycle exists in the graph or not.
# Input Format:
# Input will be the graph in the form of adjacency matrix or adjacency list.
# Output Format:
# Output will be 'Yes Cycle Exists' if cycle exists otherwise print 'No Cycle
# Exists'. Sample 1/O Problem IlI:

def has_cycle(adj, v):
    visited = [False] * v
    rec = [False] * v

    def dfs(u):
        visited[u] = True
        rec[u] = True

        for j in range(v):
            if adj[u][j] != 0:
                if not visited[j]:
                    if dfs(j):
                        return True
                elif rec[j]:
                    return True

        rec[u] = False
        return False

    for i in range(v):
        if not visited[i]:
            if dfs(i):
                return True
    return False

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

if has_cycle(adj, v):
    print("Yes Cycle Exists")
else:
    print("No Cycle Exists")