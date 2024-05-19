from Utility import FileManager as Fm
from Bean import HuffmanCoding as Hc


class Compressor:
    def __init__(self):
        pass

    def Compress(self, filename, ext, new_ext):
        #Crea el Manejador de Archivos
        fm = Fm.FileManager(filename)
        #Lee el contenido
        content = fm.read_file(ext)
        #Inicia la class Huffman con el contenido del archivo
        hc = Hc.HuffmanCoding(content)
        #Obtiene las frecuencias, crea el arbol y devuleve la cabeza del arbol
        tree = hc.build_tree()
        #Muestra el arbol como imagen
        hc.visualize_tree(tree)
        #Genera los códigos
        codes = hc.generate_codes(tree)
        #Reemplazar
        new_content = hc.replace_codes(codes)
        #Crea el nuevo archivo
        fm.create_file(new_ext)
        # Convertir string en binario
        new_content = hc.encoded(new_content)
        new_content = hc.byte_array(new_content)

        # Escribir en nuevo archivo
        fm.write_file_b(new_content, new_ext)
        print("Diccionario de codigos:\n", codes)

    def Descompress(self,filename,ext,new_ext):
        # Crea el Manejador de Archivos
        fm = Fm.FileManager(filename)
        # Lee el contenido en binario
        content = fm.read_file_b(ext)
        # Convertir contenido en bits
        content = ''.join(f'{byte:08b}' for byte in content[1:-1])

        #Obtener diccionario
        dict_huffman = {'a': '000', 's': '001', 'S': '0100', 'b': '0101', 'e': '011', 'o': '100', 'n': '1010', ' ': '1011', 'L': '11000', 'p': '11001', 't': '11010', 'i': '11011', 'r': '11100', '\n': '11101', 'z': '11110', 'O': '11111'}

        #Invertir Diccionario
        dict_huffman = {v: k for k, v in dict_huffman.items()}

        print("Diccionario inverso:\n", dict_huffman)

        print("Lectura en Binario:\n", content)
        # Recorrer contenido y reemplzar valores del diccionario
        decoded_string = ""
        buffer = ""
        for bit in content:
            buffer += bit
            if buffer in dict_huffman:
                decoded_string += dict_huffman[buffer]
                buffer = ""
        decoded_string

        print("Decodificación:\n", decoded_string)
