# Note: Input, output format along with sample input output for problem |
# and Il is same and is provided at the end of problem II.
# l. After end term examination, Akshay wants to party with his
# friends. All his friends are living as paying guest and it has been
# decided to first gather at Akshay’s house and then move towards party
# 7. | location. The problem is that no one knows the exact address of his
# house in the city. Akshay as a computer science wizard knows how to
# apply his theory subjects in his real life and came up with an amazing
# idea to help his friends. He draws a graph by looking in to location of
# his house and his friends’ location (as a node in the graph) on a map.
# He wishes to find out shortest distance and path covering that distance
# from each of his friend’s location to his house and then whatsapp them
# this path so that they can reach his house in minimum time. Akshay has
# developed the program that implements Dijkstra’s algorithm but not
# 2023-24 and 2024-25 onwards
# sure about correctness of results. Can you also implement the same
# algorithm and verify the correctness of Akshay’s results? (Hint: Print
# shortest path and distance from friends’ location to Akshay’s house)

import heapq

def dijkstra(adj, v, src):
    dist = [float('inf')] * v
    parent = [-1] * v
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        for j in range(v):
            if adj[u][j] != 0:
                if dist[j] > d + adj[u][j]:
                    dist[j] = d + adj[u][j]
                    parent[j] = u
                    heapq.heappush(pq, (dist[j], j))

    return dist, parent

def path(parent, j):
    p = []
    while j != -1:
        p.append(j)
        j = parent[j]
    return p[::-1]

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

src = int(input())

dist, parent = dijkstra(adj, v, src)

for i in range(v):
    if i != src:
        p = path(parent, i)
        print("Path:", *p)
        print("Distance:", dist[i])