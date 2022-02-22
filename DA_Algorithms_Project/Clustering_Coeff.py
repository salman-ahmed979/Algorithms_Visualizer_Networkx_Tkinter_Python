import networkx as nx

def Clustering_Coefficient(G):
    print('Local Clustering Result')
    print(nx.clustering(G))

    print('Average Clustering')
    print(nx.average_clustering(G))