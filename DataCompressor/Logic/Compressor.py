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
        print(codes)

    def Descompress(self,filename,ext,new_ext):
        # Crea el Manejador de Archivos
        fm = Fm.FileManager(filename)
        # Lee el contenido en binario
        content = fm.read_file_b(ext)
        # Convertir contenido en bits
        content = ''.join(f'{byte:08b}' for byte in content[1:-1])

        #Obtener diccionario
        dict_huffman = {'q': '000000', 'V': '00000100', 'F': '0000010100', 'L': '00000101010', 'E': '00000101011', 'S': '000001011', 'P': '00000110', 'x': '000001110', 'I': '0000011110', 'j': '0000011111', 'd': '00001', 'l': '0001', 'e': '001', 'n': '0100', 'g': '010100', 'h': '0101010', 'N': '010101100', 'M': '010101101', 'Q': '010101110', 'D': '010101111', 'v': '010110', ',': '010111', 't': '0110', 'o': '01110', 'b': '011110', '\n': '01111100', 'A': '011111010', 'C': '011111011', 'f': '0111111', 'a': '1000', 'm': '10010', 'c': '10011', ' ': '101', 's': '1100', 'r': '11010', 'p': '110110', '.': '110111', 'u': '1110', 'i': '1111'}

        #Invertir Diccionario
        dict_huffman = {v: k for k, v in dict_huffman.items()}


        print(content)
        # Recorrer contenido y reemplzar valores del diccionario
        decoded_string = ""
        buffer = ""
        for bit in content:
            buffer += bit
            if buffer in dict_huffman:
                decoded_string += dict_huffman[buffer]
                buffer = ""
        decoded_string

        print("Decoded string:", decoded_string)
