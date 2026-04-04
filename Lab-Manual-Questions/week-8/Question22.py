# l. Assume that a project of road construction to connect some
# cities is given to your friend. Map of these cities and roads which will
# connect them (after construction) is provided to him in the form of a
# graph. Certain amount of rupees is associated with construction of each
# road. Your friend has to calculate the minimum budget required for this
# project. The budget should be designed in such a way that the cost of
# connecting the cities should be minimum and number of roads required
# to connect all the cities should be minimum (if there are N cities then
# only N-1 roads need to be constructed). He asks you for help. Now, you
# have to help your friend by designing an algorithm which will find
# minimum cost required to connect these cities. (use Prim's algorithm)

import heapq

def prim(adj, v):
    visited = [False] * v
    min_heap = [(0, 0)]
    total = 0

    while min_heap:
        wt, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total += wt

        for j in range(v):
            if adj[u][j] != 0 and not visited[j]:
                heapq.heappush(min_heap, (adj[u][j], j))

    return total

v = int(input())
adj = []

for _ in range(v):
    adj.append(list(map(int, input().split())))

print(prim(adj, v))