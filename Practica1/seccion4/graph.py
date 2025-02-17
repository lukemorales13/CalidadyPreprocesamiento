import networkx as nx
import matplotlib.pyplot as plt
import pickle

def tree_layout(G, root):
    levels = {} 
    pos = {} 
    
    def dfs(node, depth=0):
        if node in levels:
            return
        levels[node] = depth
        for neighbor in G.successors(node):
            dfs(neighbor, depth + 1)
    
    dfs(root)
    
    # Agrupar nodos por niveles
    level_nodes = {}
    for node, depth in levels.items():
        level_nodes.setdefault(depth, []).append(node)
    
    # Asignar posiciones
    for depth, nodes in level_nodes.items():
        width = len(nodes)
        for i, node in enumerate(nodes):
            pos[node] = (i - width / 2, -depth)
    
    return pos


G = nx.DiGraph()
edges = [
    ("Projects", "Project_1", ''),
    ("Projects", "Project_2", ''),

    ("Project_1", "Product X", 'Name'),
    ("Project_1", "1", 'Number'),
    ("Project_1", "Bellaire", 'Location'),
    ("Project_1", "Worker_1", ''),
    ("Project_1", "Worker_2", ''),

    ("Worker_1", "123456789", 'Ssn'),
    ("Worker_1", "Smith", 'Last_name'),
    ("Worker_1", "32.5", 'Hours'),

    ("Worker_2", "435435435", 'Ssn'),
    ("Worker_2", "Joyce", 'First_name'),
    ("Worker_2", "20.0", 'Hours')
]

for edge in edges:
    G.add_edge(edge[0], edge[1], label=edge[2])

pos = tree_layout(G, "Projects")
edge_labels = nx.get_edge_attributes(G, "label")
plt.figure(figsize=(12, 7))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="gray", font_size=9, font_weight="black", arrows=True, arrowstyle='-|>')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
with open("graph.pkl", "wb") as f:
    pickle.dump(G, f)
plt.show()