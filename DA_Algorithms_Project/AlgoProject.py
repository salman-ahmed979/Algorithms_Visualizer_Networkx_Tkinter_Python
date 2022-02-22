import networkx as nx
import matplotlib.pyplot as plt
from BellmanFord import BellmanFord
from Boruvka import BoruvkaAlgo
from Clustering_Coeff import Clustering_Coefficient
from Dijsktra import Dijkstra
from FloydWarshall import FloydWarshall
from FloydWarshallPair import FloydWarshall_Pair
from Prims import Prims
from Kruskal import Kruskal_Algo

# reading nodes coordinates from the input
def convert(num):
    return float(num)


def GraphRunnerAlgorithm(file, algo):
    fileOpener = "./" + file
    # read data
    data = open(fileOpener, "r")
    data = str(data.read())
    # filter by line
    lines = data.split("\n")
    
    filtered = []

    # filter by unwanted newlines
    for line in lines:
        newFilter = line.replace("\r", "")
        if newFilter != "" and newFilter != "NETSIM":
            filtered.append(newFilter)

    nodeNo = int(filtered.pop(0))
    startingNode = int(filtered.pop())
    nodes = []

    for i in range(nodeNo):
        node = filtered.pop(0)
        node = node.split("\t")
        # print(node)
        node = [float(i) for i in node]
        nodes.append(node)

    # reading edges from the input

    graph = []
    for i in range(nodeNo):
        arr = []
        for j in range(nodeNo):
            arr.append(0)
        graph.append(arr)


    for line in filtered:
        line = line.split("\t")
        #   to remove last ""
        line.pop()

        from_node = int(line.pop(0))
        for i in range(0, len(line), 4):
            if graph[int(line[i])][from_node] == 0:
                graph[from_node][int(line[i])] = float(line[i + 2]) / 10000000
                graph[int(line[i])][from_node] = float(line[i + 2]) / 10000000
            elif graph[from_node][int(line[i])] > (float(line[i + 2]) / 10000000):
                graph[from_node][int(line[i])] = float(line[i + 2]) / 10000000
                graph[int(line[i])][from_node] = float(line[i + 2]) / 10000000
    
    # Networkx Graph Creation
    G = nx.Graph()
    
    # Adding Nodes on Graph
    size = graph.__len__()
    for i in range(size):
        G.add_node(i, pos=(nodes[i][1], nodes[i][2]))
    
    
    parent = []

    # Conditions for Different Algorithms
    if algo == 'Prims':
        parent = Prims(G, graph, size, startingNode)
    
    elif algo == 'Kruskal':
        parent = Kruskal_Algo(G, graph, size)
    
    elif algo == 'Dijsktra':
        parent = Dijkstra(graph, size, startingNode)
    
    elif algo == 'BellmanFord':
        parent = BellmanFord(graph, size, startingNode)
    
    elif algo == 'Boruvka':
        BoruvkaAlgo(G, graph, size)
    
    elif algo == 'ClusteringCoefficient':
        # Print the Graph
        for i in range(size):
            for j in range(size):
                if graph[i][j] != 0 and i != j:
                    G.add_edge(i, j, weight=graph[i][j])
        # Calling Function
        Clustering_Coefficient(G)
    elif algo == 'FloydWarshall':
        FloydWarshall_Pair(G, graph, size)
        # FloydWarshall(G, graph, size, startingNode)
    else:
        print('Algo not found')

    # Cost COmpt
    cost = 0.0
    # Check if parent[] exist
    print(parent)
    if parent.__len__() != 0:
        for i in range(size):
            if parent[i] != -1:
                cost += graph[parent[i]][i]
                G.add_edge(parent[i], i, weight=graph[parent[i]][i])
    
    if parent.__len__():
        print('Cost: ', cost)
    # Get Edge and Node
    edge_weight=nx.get_edge_attributes(G,'weight')
    node_pos = nx.get_node_attributes(G, 'pos')

    # Draw Nodes
    nx.draw(G, node_pos, with_labels=True, edge_color='red', node_color="lightblue", node_size=600,
    arrows=False, font_size=7, font_family='sans-serif', linewidths=0.2)

    # Draw Edges

    nx.draw_networkx_edge_labels(G, node_pos, edge_labels=edge_weight, label_pos=0.5, font_size=8,font_family="sans-serif", horizontalalignment="left")
    
    plt.show()
    
