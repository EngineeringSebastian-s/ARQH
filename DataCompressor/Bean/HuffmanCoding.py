import os

from graphviz import *

from Bean.Node import Node


class HuffmanCoding:
    content = ""
    tree = None
    codes = {}

    # Constructor
    def __init__(self, content):
        self.content = content

    # Metodo de Compresión

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

    def build_tree(self, nodes):
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

        self.tree = nodes[0]  # Cabeza del arbol

    def serialize_tree(self, node):
        if node is None:
            return ""
        if node.char is not None:
            return f'1{node.char}'
        return f'0{self.serialize_tree(node.left)}{self.serialize_tree(node.right)}'

    def add_tree(self):
        serialized_tree = self.serialize_tree(self.tree)
        tree_length = len(serialized_tree)
        # Convert tree_length to a fixed-size 4-byte string representation
        length_prefix = f'{tree_length:04}'
        info_tree = length_prefix + serialized_tree
        info_tree = ''.join(format(ord(char), '08b') for char in info_tree)
        self.content = info_tree + self.content

    def generate_codes(self, node, path="", code={}):
        if node is not None:
            if node.char is not None:
                code[node.char] = path
            self.generate_codes(node.left, path + "0", code)
            self.generate_codes(node.right, path + "1", code)
        self.codes = code

    def replace_codes(self):
        new_content = ""
        for char in self.content:
            if char in self.codes:
                new_content += self.codes[char]
        self.content = new_content

    def encoded(self):
        ext_bit = 8 - len(self.content) % 8  # Calcular la cantidad de bits faltantes
        for i in range(ext_bit):
            self.content += "0"
        format_bin = "{0:08b}".format(ext_bit)
        self.content = format_bin + self.content

    def byte_array(self):
        b = bytearray()
        for i in range(0, len(self.content), 8):
            byte = self.content[i:(i + 8)]
            b.append(int(byte, 2))
        self.content = b

    # Metodo de Descompresión
    def decode(self):
        decode_content = ""
        for byte in self.content:
            decode_content += f'{byte:08b}'
        padding_length = int(decode_content[:8], 2)
        decode_content = decode_content[8:-padding_length]
        self.content = decode_content

    def generate_codes_invert(self, node):
        self.generate_codes(node)
        self.codes = {v: k for k, v in self.codes.items()}

    def replace_codes_bit(self):
        decoded_string = ""
        buffer = ""
        for bit in self.content:
            buffer += bit
            if buffer in self.codes:
                decoded_string += self.codes[buffer]
                buffer = ""
        self.content = decoded_string

    def rebuild_tree(self):
        binary_length_prefix = self.content[:32]
        length_prefix = ''.join(
            chr(int(binary_length_prefix[i:i + 8], 2)) for i in range(0, len(binary_length_prefix), 8))
        tree_length = int(length_prefix)
        binary_serialized_tree = self.content[32:32 + tree_length * 8]
        serialized_tree = ''.join(
            chr(int(binary_serialized_tree[i:i + 8], 2)) for i in range(0, len(binary_serialized_tree), 8))
        self.tree = self.deserialize_tree(iter(serialized_tree))
        self.content = self.content[32 + tree_length * 8:]

    def deserialize_tree(self, data_iter):
        val = next(data_iter)
        if val == '1':
            char = next(data_iter)
            return Node(char, None)
        node = Node(None, None)
        node.left = self.deserialize_tree(data_iter)
        node.right = self.deserialize_tree(data_iter)
        return node

    # Metodos de Impresión

    def print_tree(self, node, indent=""):
        if node is not None:
            print(indent + str(node.freq) + (": " + node.char if node.char else ": None"))
            self.print_tree(node.left, indent + "  ")
            self.print_tree(node.right, indent + "  ")

    def visualize_tree(self):
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

        try:
            graph = Digraph()
            add_nodes_edges(self.tree, graph)
            graph.render(os.path.join(os.getcwd(), "View", "huffman_tree"), format='png', view=True)
            print("Renderizado exitoso.")
        except ExecutableNotFound as e:
            print(f"Error: No se encontró Graphviz. Asegúrate de que Graphviz esté instalado y en el PATH del "
                  f"sistema.\nDetalles: {e}")
        except CalledProcessError as e:
            print(f"Error: Hubo un problema al ejecutar Graphviz.\nDetalles: {e}")
        except RequiredArgumentError as e:
            print(f"Error: Argumento requerido faltante.\nDetalles: {e}")
        except Exception as e:
            print(f"Error: Se produjo un error inesperado.\nDetalles: {e}")
