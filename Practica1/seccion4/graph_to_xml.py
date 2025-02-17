import xml.etree.ElementTree as ET
import xml.dom.minidom
import networkx as nx
import pickle

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

with open("graph.pkl", "rb") as f:
    G = pickle.load(f)

xml_output = tree_to_xml(G, 'Projects')
print(xml_output)