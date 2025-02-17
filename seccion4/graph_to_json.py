import networkx as nx
import json
import pickle

def tree_to_json(graph: nx.DiGraph, root: str) -> str:
    """
    Convierte un árbol dirigido de networkx en un formato JSON estructurado jerárquicamente,
    utilizando las etiquetas de las aristas como claves cuando están disponibles.
    
    :param graph: Grafo dirigido de networkx
    :param root: Nodo raíz del árbol
    :return: Representación JSON del árbol
    """
    def build_tree(node):
        children = list(graph.successors(node))  # Obtener hijos del nodo
        
        if not children:
            return node  # Nodo hoja
        
        tree_structure = {}
        for child in children:
            edge_label = graph.edges[node, child].get('label', '')
            child_tree = build_tree(child)
            
            if edge_label:
                if edge_label not in tree_structure:
                    tree_structure[edge_label] = {}
                tree_structure[edge_label][child] = child_tree
            else:
                tree_structure[child] = child_tree
        
        return tree_structure

    # Guardar el XML en un archivo
    with open('graph.json', "w", encoding="utf-8") as f:
        f.write(json.dumps({root: build_tree(root)}, indent=2))

    return f"JSON guardado en graph.json"

with open("graph.pkl", "rb") as f:
    G = pickle.load(f)

tree_json = tree_to_json(G, 'Projects')
print(tree_json)