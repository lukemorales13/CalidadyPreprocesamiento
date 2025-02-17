# inciso a)

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

# inciso b)

def matriz_adjacencia(num_nodos, aristas):
    matriz = [[0] * num_nodos for _ in range(num_nodos)] # Matriz de ceros
    for arista in aristas:
        p, q = arista
        matriz[p-1][q-1] = 1 # se resta 1 porque las listas inician en 0
        matriz[q-1][p-1] = 1 # También es 1 ya que en este caso, la gráfica es no dirigida
    return matriz

matriz_de_adjacencia = matriz_adjacencia(num_nodos = 9, aristas = aristas)

for _ in matriz_de_adjacencia:
    print(_)