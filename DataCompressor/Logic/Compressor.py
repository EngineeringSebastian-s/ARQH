from Utility import FileManager as Fm
from Bean import HuffmanCoding as Hc


class Compressor:
    def __init__(self):
        pass

    def Compress(self, filename, ext, new_ext):
        fm = Fm.FileManager(filename)
        content = fm.read_file(ext)
        hc = Hc.HuffmanCoding(content)
        frequency = hc.make_frecuency()
        hc.build_tree(frequency)
        hc.visualize_tree()
        hc.generate_codes(hc.tree)
        hc.replace_codes()
        fm.create_file(new_ext)
        hc.add_tree()
        hc.encoded()
        hc.byte_array()
        fm.write_file_b(hc.content, new_ext)
        print("Diccionario de codigos:\n", hc.codes)

    def Descompress(self, filename, ext):
        fm = Fm.FileManager(filename)
        content = fm.read_file_b(ext)
        hc = Hc.HuffmanCoding(content)
        print(content)
        hc.decode()
        print(hc.content)
        hc.rebuild_tree()
        hc.visualize_tree()
        hc.generate_codes_invert(hc.tree)
        hc.replace_codes_bit()
        fm.write_file(hc.content, ".txt")
        print("Diccionario inverso:\n", hc.codes)
        print("Lectura en Binario:\n", content)
        print("Decodificación:\n", hc.content)
