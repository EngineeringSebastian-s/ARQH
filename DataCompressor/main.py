from Logic import Compressor as Cm

if __name__ == '__main__':
    cm = Cm.Compressor()
    #cm.Compress("Archivo", ".txt", ".slo")
    cm.Descompress("Archivo", ".slo", ".txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


