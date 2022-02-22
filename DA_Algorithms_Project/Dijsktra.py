
MAX = 1000000000000
def minDistance(dist, visited, size):
    min = MAX
    min_index = -1
    # Search not in shortest path
    for u in range(size):
        if (dist[u] < min and visited[u] == False):
            min = dist[u]
            min_index = u
    return min_index

def Dijkstra(graph, size, startNode):
    dist = [MAX] * size
    parent = [-1] * size
    
    dist[startNode] = 0
    visited = [False] * size
    
    for count in range(size):
        x = minDistance(dist,visited, size)

        visited[x] = True

        for y in range(size):
            if graph[x][y] > 0 and visited[y] == False and dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
                parent[y] = x
                if y == 4:
                    break
    return parent
