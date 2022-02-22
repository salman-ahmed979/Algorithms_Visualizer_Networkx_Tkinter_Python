MAXPATH = 1000000
def FloydWarshall_Pair(G, graph, size):
    dist = [[0]*size]*size
    
    # Initialize Path
    for i in range(size):
        for j in range(size):
            dist[i][j] = graph[i][j]

            # No edge 
            if graph[i][j] == 0:
                dist[i][j] = MAXPATH
    
    for k in range(size):
        for i in range(size):
            for j in range(size):

                # No edge exist
                if dist[i][k] == MAXPATH or dist[k][j] == MAXPATH:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # Cost
    cost = 0.0
    for i in range(size):
        for j in range(size):
            if dist[i][j] != MAXPATH and i != j:
                cost += dist[i][j]
                G.add_edge(i, j, weight=dist[i][j])
    print('Cost: ', cost)