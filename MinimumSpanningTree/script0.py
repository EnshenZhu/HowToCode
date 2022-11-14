# Use the Prim's algorithm to create a minimum spanning tree from a connected, undirected graph

"""
This script is derived from https://www.youtube.com/watch?v=5ZYBFcPSvvE&ab_channel=CodeSavant

Steps:
Start at any vertex
While MST isn't full:
    - Go through each vertex currently in the MST
    - Get its smallest edge whose destination isn't in MST
    - Pick the smallest edge out of all smallest edges
    - Add this edge to MST, mark its vertices as used
Print MST
"""

import heapq

mst = []
usedVertices = set()

with open(r"Prime_MST_input.txt") as f:
    numVertices = int(f.readline())
    all_edges = [[] for _ in range(numVertices)]

    for line in f.readlines():
        edge = tuple(map(int, line.split(" ")))

        if edge[0] == edge[1]: continue  # the edge is self looped

        heapq.heappush(all_edges[edge[0]], (edge[2], edge[1]))
        # print(all_edges)

        heapq.heappush(all_edges[edge[1]], (edge[2], edge[0]))

    print(all_edges)

cost, dest = 0, 1
while len(usedVertices) < numVertices:  # when not all vertices have been used
    vertexWithSmallestEdge = 0
    for vertex in usedVertices:
        while len(all_edges[vertex]) > 0 and all_edges[vertex][0][dest] in usedVertices:
            heapq.heappop(all_edges[vertex])

        if len(all_edges[vertex]) == 0: continue

        if len(all_edges[vertexWithSmallestEdge]) == 0 \
                or all_edges[vertex][0][cost] < all_edges[vertex][vertexWithSmallestEdge][cost]:
            vertexWithSmallestEdge = vertex
    edge = heapq.heappop(all_edges[vertexWithSmallestEdge])
    mst.append((vertexWithSmallestEdge, edge[dest], edge[cost]))

    usedVertices.add(vertexWithSmallestEdge)
    usedVertices.add(edge[dest])

print(mst)
