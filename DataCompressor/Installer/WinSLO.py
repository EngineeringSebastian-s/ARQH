import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QApplication
from graphviz import *


# View

class TextLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Suelta el archivo de texto aquí \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa;
                padding: 10px;
                word-wrap: break-word;
            }
        ''')
        self.setWordWrap(True)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.textViewer = TextLabel()
        mainLayout.addWidget(self.textViewer)

        self.actionButton = QPushButton("Comprimir/Descomprimir", self)
        self.actionButton.setEnabled(False)
        self.actionButton.clicked.connect(self.performAction)
        mainLayout.addWidget(self.actionButton)

        self.setLayout(mainLayout)

        self.filePath = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and (urls[0].toLocalFile().endswith('.txt') or urls[0].toLocalFile().endswith('.slo')):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and (urls[0].toLocalFile().endswith('.txt') or urls[0].toLocalFile().endswith('.slo')):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and (urls[0].toLocalFile().endswith('.txt') or urls[0].toLocalFile().endswith('.slo')):
                event.setDropAction(Qt.CopyAction)
                self.filePath = urls[0].toLocalFile()
                try:
                    self.set_text(self.filePath)
                    self.updateButton()
                    event.accept()
                except Exception as e:
                    self.showAlert(f"Error al abrir el archivo: {e}")
                    event.ignore()
            else:
                event.ignore()
        else:
            event.ignore()

    def set_text(self, file_path):
        try:
            if file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    content = file.read()
            elif file_path.endswith('.slo'):
                with open(file_path, 'rb') as file:
                    content = file.read()
                content = content.decode('utf-8', errors='ignore')  # Decodificar si es necesario
            self.textViewer.setText(content)
        except Exception as e:
            raise e

    def updateButton(self):
        if self.filePath.endswith('.txt'):
            self.actionButton.setText("Comprimir")
        elif self.filePath.endswith('.slo'):
            self.actionButton.setText("Descomprimir")
        self.actionButton.setEnabled(True)

    def showAlert(self, message, title="Alerta"):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def performAction(self):
        if self.filePath.endswith('.txt'):
            self.compress()
        elif self.filePath.endswith('.slo'):
            self.decompress()

    def compress(self):
        try:
            file_dir = os.path.dirname(self.filePath)
            file_root, file_ext = os.path.splitext(self.filePath)
            file_name = os.path.basename(file_root)
            cm = Compressor()
            cm.Compress(file_name, file_dir)
            QMessageBox.information(self, "Acción",
                                    f"Archivo '{file_name}{file_ext}' comprimido con éxito en: {file_dir}")
        except Exception as e:
            self.showAlert(f"Error al comprimir el archivo {file_name}{file_ext}: {e}")

    def decompress(self):
        try:
            file_dir = os.path.dirname(self.filePath)
            file_root, file_ext = os.path.splitext(self.filePath)
            file_name = os.path.basename(file_root)
            cm = Compressor()
            cm.Descompress(file_name, file_dir)
            QMessageBox.information(self, "Acción",
                                    f"Archivo '{file_name}{file_ext}' descomprimido con éxito en: {file_dir}")
        except Exception as e:
            self.showAlert(f"Error al descomprimir el archivo {file_name}{file_ext}: {e}")


# Bean
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

        try:
            graph = Digraph()
            add_nodes_edges(self.tree, graph)
            graph.render(os.path.join(root, "huffman_tree"), format='png', view=True)
            print("Renderizado exitoso.")
        except ExecutableNotFound as e:
            print(
                f"Error: No se encontró Graphviz. Asegúrate de que Graphviz esté instalado y en el PATH del "
                f"sistema.\nDetalles: {e}")
        except CalledProcessError as e:
            print(f"Error: Hubo un problema al ejecutar Graphviz.\nDetalles: {e}")
        except RequiredArgumentError as e:
            print(f"Error: Argumento requerido faltante.\nDetalles: {e}")
        except Exception as e:
            print(f"Error: Se produjo un error inesperado.\nDetalles: {e}")


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


# Logic

class Compressor:
    def __init__(self):
        pass

    def Compress(self, filename, root):
        fm = FileManager(filename, root)
        hc = HuffmanCoding(fm.read_file())
        if hc.content != "":
            frequency = hc.make_frecuency()
            hc.build_tree(frequency)
            hc.visualize_tree(root)
            hc.generate_codes(hc.tree)
            hc.replace_codes()
            fm.create_file()
            hc.add_tree()
            hc.encoded()
            hc.byte_array()
            fm.write_file_b(hc.content)
            print("Diccionario de codigos:\n", hc.codes)
        else:
            raise Exception(f"El archivo esta vacio")

    def Descompress(self, filename, root):
        fm = FileManager(filename, root)
        hc = HuffmanCoding(fm.read_file_b())
        if hc.content != "":
            print("Lectura en Binario:\n", hc.content)
            hc.decode()
            print("Lectura en Representación Binaria:\n", hc.content)
            hc.rebuild_tree()
            hc.visualize_tree(root)
            hc.generate_codes_invert(hc.tree)
            hc.replace_codes_bit()
            fm.write_file(hc.content)
            print("Diccionario inverso:\n", hc.codes)
            print("Decodificación:\n", hc.content)
        else:
            raise Exception(f"El archivo esta vacio")


# Utility

class FileManager:
    def __init__(self, filename, root=os.getcwd()):
        self.filename = filename
        self.root = root

    def read_file(self):
        try:
            with open(os.path.join(self.root, self.filename + ".txt"), "r", encoding='utf-8') as file:
                return file.read().rstrip()
        except OSError or FileNotFoundError as e:
            print("Error al leer el archivo:", e)
        return ""

    def write_file(self, content):
        try:
            with open(os.path.join(self.root, self.filename + "_unslo.txt"), 'w', encoding='utf-8') as file:
                file.write(content)
        except OSError or FileNotFoundError as e:
            print("Error al escribir en el archivo:", e)

    def create_file(self):
        try:
            with open(os.path.join(self.root, self.filename + ".slo"), 'x') as f:
                print(f"Archivo creado exitosamente.")
        except FileExistsError:
            print("El archivo ya existe")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def read_file_b(self):
        try:
            with open(os.path.join(self.root, self.filename + ".slo"), "rb") as file:
                return file.read()
        except OSError or FileNotFoundError as e:
            print("Error al leer el archivo:", e)
        return ""

    def write_file_b(self, content):
        try:
            with open(os.path.join(self.root, self.filename + ".slo"), 'wb') as file:
                file.write(bytes(content))
        except OSError or FileNotFoundError as e:
            print("Error al escribir en el archivo:", e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Application()
    frame.show()
    sys.exit(app.exec_())
