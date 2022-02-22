

# Find the Set of i
def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

# Union of two set x and y as per rank
def union(parent, i, j):
    u = find(parent, i)
    v = find(parent, j)
    parent[u] = v

#Kruskal Algorithm -- Spanning Tree Finder
def Kruskal_Algo(G, graph, size):
    # Initialize disjoint
    parent = [0] * size
    result_parent = [0] * size
    
    for i in range(size):
        parent[i] = i
        result_parent[i] = -1
    
    edg_count = 0
    while (edg_count < size - 1):
        min = 10000000000000
        u = -1
        v = -1
        for i in range(size):
            for j in range(size):
                if graph[i][j] != 0 and find(parent, i) != find(parent, j) and graph[i][j] < min:
                    min = graph[i][j]
                    u = i
                    v = j
        union(parent, u, v)
        # G.add_edge(u, v, weight=graph[u][v])
        # Getting Parent weight
        if result_parent[v] == -1:
            result_parent[v] = u
        else:
            result_parent[u] = v
            
        edg_count += 1
    return result_parent