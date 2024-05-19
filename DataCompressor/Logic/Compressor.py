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
        content = ''.join(f'{byte:08b}' for byte in content)


        #Obtener diccionario
        dict_huffman = {'a': '00', '\n': '0100', 'd': '01010', 'y': '01011', ' ': '011', 'm': '10000', 'i': '10001', 'n': '10010', 'C': '10011', 't': '10100', 'B': '10101', 'A': '10110', 'z': '10111', 'o': '1100', 'e': '1101', 'J': '11100', 'u': '11101', 'l': '1111'}


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
