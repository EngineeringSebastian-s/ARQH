from Bean.Node import Node
from graphviz import Digraph
import os


class HuffmanCoding:
    def __init__(self, content):
        self.content = content

    def make_frecuency(self):
        frequency = {}
        for char in self.content:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        # Crear Lista con objetos Nodo en cada posición, ordenado con una función incognita
        return sorted((Node(char, freq) for char, freq in frequency.items()), key=lambda node: node.freq)

    def insert_node(self, nodes, new_node):
        # Busca el lugar para insertar el nodo de forma ascendente con menor prioridad
        index = 0
        while index < len(nodes) and new_node.freq > nodes[index].freq:
            index += 1
        nodes.insert(index, new_node)

    def build_tree(self):
        nodes = self.make_frecuency()
        while len(nodes) > 1:
            # Nodos de menor frecuencia
            left = nodes.pop(0)
            right = nodes.pop(0)

            # Crear Nodo Cabeza de los nodos hijos
            merge_freq = left.freq + right.freq
            merged_node = Node(None, merge_freq)
            merged_node.left = left
            merged_node.right = right

            # Insertar el nuevo nodo en la lista de forma ascendente
            self.insert_node(nodes, merged_node)

        return nodes[0]  # Cabeza del arbol

    def generate_codes(self, node, path="", code={}):
        if node is not None:
            if node.char is not None:
                code[node.char] = path
            self.generate_codes(node.left, path + "0", code)
            self.generate_codes(node.right, path + "1", code)
        return code

    def replace_codes(self, codes):
        new_content = ""
        for char in self.content:
            if char in codes:
                new_content += codes[char]
        return new_content

    def encoded(self, content):
        ext_bit = 8 - len(content) % 8 # Calcular la cantidad de bits faltantes
        for i in range(ext_bit):
            content += "0"
        format_bin = "{0:08b}".format(ext_bit)
        content = format_bin + content
        return content
    def byte_array(self,content):
        b = bytearray()
        for i in range(0, len(content),8):
            byte = content[i:(i+8)]
            b.append(int(byte, 2))
        return b

    def print_tree(self, node, indent=""):
        if node is not None:
            print(indent + str(node.freq) + (": " + node.char if node.char else ": None"))
            self.print_tree(node.left, indent + "  ")
            self.print_tree(node.right, indent + "  ")

    def visualize_tree(self, root):
        def add_nodes_edges(node, graph):
            if node is not None:
                if node.char:
                    graph.node(name=str(id(node)), label=f"{node.char}:{node.freq}")
                else:
                    graph.node(name=str(id(node)), label=f":{node.freq}")

                if node.left:
                    add_nodes_edges(node.left, graph)
                    graph.edge(str(id(node)), str(id(node.left)), label="0")

                if node.right:
                    add_nodes_edges(node.right, graph)
                    graph.edge(str(id(node)), str(id(node.right)), label="1")

        graph = Digraph()
        add_nodes_edges(root, graph)
        graph.render(os.path.join(os.getcwd(), "View", "huffman_tree"), format='png', view=True)
