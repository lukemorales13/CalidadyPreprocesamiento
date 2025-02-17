import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom

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


def tree_to_xml(graph: nx.DiGraph, root: str) -> str:
    """
    Convierte un árbol dirigido de networkx en una estructura XML,
    utilizando las etiquetas de las aristas como nombres de etiquetas cuando están disponibles.
    
    :param graph: Grafo dirigido de networkx
    :param root: Nodo raíz del árbol
    :return: Representación XML en formato de cadena
    """
    def build_xml_element(node):
        children = list(graph.successors(node))
        
        if not children:
            return ET.Element(node)  # Nodo hoja sin hijos
        
        element = ET.Element(node)
        for child in children:
            edge_label = graph.edges[node, child].get('label', '')
            child_element = build_xml_element(child)
            
            if edge_label:
                tag = ET.Element(edge_label)
                tag.text = child
                element.append(tag)
            else:
                element.append(child_element)
        
        return element
    
    root_element = build_xml_element(root)

    xml_str = ET.tostring(root_element, encoding='utf-8').decode('utf-8')
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="    ")

    print(pretty_xml)

    # Guardar el XML en un archivo
    with open('graph.xml', "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    return f"XML guardado en graph.xml"


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

tree_json = tree_to_json(G, 'Projects')
xml_output = tree_to_xml(G, 'Projects')
print(xml_output)
print(tree_json)
plt.show()