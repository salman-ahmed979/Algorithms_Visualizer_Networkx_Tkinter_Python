
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

def BoruvkaAlgo(G, graph, size):
    parent = []
    rank = []
    cheapest = []
    mstCost = 0.0
    for node in range(size):
        parent.append(node)
        rank.append(0)
        cheapest = [-1]*size
    
    numTrees = size

    while(numTrees > 1):

        for i in range(size):
            for j in range(size):
                if graph[i][j] != 0:
                    w = graph[i][j]
                    set1 = find(parent, i)
                    set2 = find(parent, j)

                    if set1 != set2:
                        if cheapest[set1] == -1 or cheapest[set1][2] > w :
                            cheapest[set1] = [i,j,w] 
  
                        if cheapest[set2] == -1 or cheapest[set2][2] > w :
                            cheapest[set2] = [i,j,w]
        for node in range(size):
            if cheapest[node] != -1:
                i,j,w = cheapest[node]
                set1 = find(parent, i)
                set2 = find(parent, j)

                if set1 != set2:
                    union(parent, rank, set1, set2)
                    # if G.has_edge(i, j):
                    mstCost += w
                    G.add_edge(i, j, weight=w)
                    numTrees = numTrees - 1
        
        cheapest = [-1]*size
    print('Cost: ', mstCost)
