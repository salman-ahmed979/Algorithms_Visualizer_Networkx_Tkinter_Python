MAX = 10000000000
def BellmanFord(graph, size, startNode):
    dist = [MAX] * size

    dist[startNode] = 0

    parent = [-1] * size
    for u in range(size - 1):
        for v in range(size):
            if graph[u][v] != 0 and dist[u] != MAX and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
    return parent