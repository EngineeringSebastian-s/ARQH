from Bean import HuffmanCoding as Hc
from Utility import FileManager as Fm


class Compressor:
    def __init__(self):
        pass

    def Compress(self, filename, root):
        fm = Fm.FileManager(filename, root)
        hc = Hc.HuffmanCoding(fm.read_file())
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
        fm = Fm.FileManager(filename, root)
        hc = Hc.HuffmanCoding(fm.read_file_b())
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
