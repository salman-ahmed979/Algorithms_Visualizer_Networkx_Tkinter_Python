MAXPATH = 1000000

def getPath(u, v, nextPath):
    if nextPath[u][v] == -1:
        print('NO PATH')
        return {}
    path = [u]
    while u != v:
        u = nextPath[u][v]
        path.append(u)
    return path

def FloydWarshall(G, graph, size, startNode):
    dist = [[0]*size]*size
    NextPath = [[0]*size]*size
    
    # Initialize Path
    for i in range(size):
        for j in range(size):
            dist[i][j] = graph[i][j]

            # No edge 
            if graph[i][j] == 0:
                dist[i][j] = MAXPATH
                NextPath[i][j] = -1
            else:
                NextPath[i][j] = j
    
    for k in range(size):
        for i in range(size):
            for j in range(size):

                # No edge exist
                if dist[i][k] == MAXPATH or dist[k][j] == MAXPATH:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    NextPath[i][j] = NextPath[i][k]
    
    path = getPath(startNode, size-1, NextPath)
    
    print(path)
    # n = len(path)
    # for i in range(n - 1):
    #     print(path[i], end=" -> ")
    # print(path[n-1])

