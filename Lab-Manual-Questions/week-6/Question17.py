# Given a graph, design an algorithm and implement it using a
# program to find if a graph is bipartite or not. (Hint: use BFS)
# Input Format:
# Input will be the graph in the form of adjacency matrix or adjacency list.
# Output Format:
# Output will be 'Yes Bipartite' if graph is bipartite, otherwise print 'Not
# Bipartite'. Sample 1/O Problem II:

from collections import deque

def is_bipartite(adj, v):
    color = [-1] * v
    
    for i in range(v):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            
            while queue:
                u = queue.popleft()
                
                for j in range(v):
                    if adj[u][j] != 0:
                        if color[j] == -1:
                            color[j] = 1 - color[u]
                            queue.append(j)
                        elif color[j] == color[u]:
                            return False
    return True

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

if is_bipartite(adj, v):
    print("Yes Bipartite")
else:
    print("Not Bipartite")