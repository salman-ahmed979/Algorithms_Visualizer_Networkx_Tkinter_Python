import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()        

import networkx as nx

G = nx.Graph()
G.add_node(1, pos=(3.2, 5.0))
G.add_node(2, pos=(10.3,20.2))
G.add_edge(1,2, weight=6)
print(G)

# Gr = nx.cubical_graph()
# subax1 = plt.subplot(121)
# nx.draw(Gr) # default spring_layout
# subax2 = plt.subplot(122)
# nx.draw(Gr, pos=nx.circular_layout(Gr), node_color='r', edge_color='b')
node_pos=nx.get_node_attributes(G,'pos')
nx.draw_networkx(G, node_pos, arrows=None, with_labels=True)
plt.axis('on')
plt.show()