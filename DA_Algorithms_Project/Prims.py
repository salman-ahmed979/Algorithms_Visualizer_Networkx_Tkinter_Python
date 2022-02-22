import networkx as nx

INT_MAX = 1000000000000000

def minKey(key, mstSet, size):
    min = INT_MAX
    min_index = -1
    for v in range(size):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index

def Prims(G, graph, size, startNode):
    key = [INT_MAX] * size
    mstSet = [False] * size
    parent = [None] * size
    #Starting Node
    key[startNode] = 0
    parent[startNode] = -1
    for count in range(size):
        u = minKey(key,mstSet,size)
        mstSet[u] = True
    
        for v in range(size):
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                # # Check if already edge is created
                # if(G.has_edge(u, v) == True):
                #     G.remove_edge(u, v)
                # else:
                #     G.add_edge(u, v, weight=key[v])
                parent[v] = u
    return parent