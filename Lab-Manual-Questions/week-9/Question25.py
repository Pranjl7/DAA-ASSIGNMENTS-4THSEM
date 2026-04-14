# l. Given a graph, Design an algorithm and implement it using a
# program to implement Floyd- Warshall all pair shortest path algorithm.
# Input Format:
# The first line of input takes number of vertices in the graph.
# Input will be the graph in the form of adjacency matrix or adjacency list.
# If a direct edge is not present between any pair of vertex (u,v), then this
# entry is shown as AdjM[u,v] = INF.
# Output Format:
# 9. Output will be shortest distance matrix in the form of V X V matrix,
# where each entry (u,v) represents shortest distance between vertex u
# and vertex v.
# Sample 1/O Problem I:
# Input: Output:
# 5 Shortest Distance Matrix:
# 01055INF 01015515
# INFO555 INFO555
# INF INF O INF 10 INFINFO 1510
# INF INF INF 020 INF INF INF 0 20
# INF INF IN5F 0 INF INF INF 50

v = int(input())
adj = []

for _ in range(v):
    row = input().split()
    temp = []
    for x in row:
        if x == "INF":
            temp.append(float('inf'))
        else:
            temp.append(int(x))
    adj.append(temp)

dist = [i[:] for i in adj]

for k in range(v):
    for i in range(v):
        for j in range(v):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(v):
    for j in range(v):
        if dist[i][j] == float('inf'):
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()