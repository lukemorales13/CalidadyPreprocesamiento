# inciso a

import networkx as nx
import matplotlib.pyplot as plt

coordenadas = {1: (2.8, 1),  2: (2, 1),  3: (1.5, 2),  4: (1, 1), 5: (1.4, 3),  6: (3, 0), 7: (4, -1), 8: (-.3, 1.3), 9: (0, 0)}

G = nx.Graph()

aristas = [(1, 2), (2, 3), (2, 4), (3, 5), (4, 8), (4, 9), (3, 4), (1, 6), (6, 7), (2,6)]
G.add_edges_from(aristas)

plt.figure(figsize=(8, 6))
nx.draw(G, pos=coordenadas, with_labels=True, node_color="red", node_size=800, edge_color="black", font_size=18)

plt.title("Figura 1")
plt.show()
