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
        new_content = bytes(new_content)
        # Escribir en nuevo archivo
        fm.write_file_b(new_content, new_ext)
        print(codes)

    def Descompress(self,filename,ext,new_ext):
        # Crea el Manejador de Archivos
        fm = Fm.FileManager(filename)
        # Lee el contenido
        content = fm.read_file(ext)
        dict_huffman = {'e': '000', 'd': '00100', 'N': '00101000', 'I': '001010010', 'A': '001010011', 'Q': '0010101000', ';': '001010100100', 'O': '0010101001010', 'L': '0010101001011', 'E': '00101010011', 'x': '001010101', '\n': '00101011', ',': '001011', 'r': '0011', 'n': '0100', 'l': '0101', 'v': '011000', 'f': '0110010', 'S': '011001100', 'D': '011001101', 'M': '011001110', 'j': '0110011110', 'C': '0110011111', 'c': '01101', 's': '0111', 'a': '1000', 't': '1001', 'o': '10100', 'p': '101010', '.': '101011', 'u': '1011', ' ': '110', 'm': '11100', 'h': '11101000', 'F': '11101001000', 'U': '11101001001', 'V': '1110100101', 'P': '111010011', 'b': '1110101', 'q': '1110110', 'g': '1110111', 'i': '1111'}
        dict_huffman = {v: k for k, v in dict_huffman.items()}

        print(content)
        def decodificar_huffman(encoded_bits, reverse_huffman_codes):
            decoded_string = ""
            buffer = ""
            for bit in encoded_bits:
                buffer += bit
                if buffer in reverse_huffman_codes:
                    decoded_string += reverse_huffman_codes[buffer]
                    buffer = ""
            return decoded_string

        # Decodificar los bits
        decoded_string = decodificar_huffman(content, dict_huffman)
        print("Decoded string:", decoded_string)
