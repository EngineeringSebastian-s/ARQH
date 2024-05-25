import os

class FileManager:
    def __init__(self, filename, root=os.getcwd()):
        self.filename = filename
        self.root = root



    def read_file(self):
        try:
            with open(os.path.join(self.root, self.filename+".txt"), "r", encoding='utf-8') as file:
                return file.read()
        except OSError or FileNotFoundError as e:
            print("Error al leer el archivo:", e)
        return ""

    def write_file(self, content):
        try:
            with open(os.path.join(self.root, self.filename+".txt"), 'w', encoding='utf-8') as file:
                file.write(content)
        except OSError or FileNotFoundError as e:
            print("Error al escribir en el archivo:", e)

    def create_file(self):
        try:
            with open(os.path.join(self.root, self.filename+".slo"), 'x') as f:
                print(f"Archivo creado exitosamente.")
        except FileExistsError:
            print("El archivo ya existe")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def read_file_b(self):
        try:
            with open(os.path.join(self.root, self.filename+".slo"), "rb") as file:
                return file.read()
        except OSError or FileNotFoundError as e:
            print("Error al leer el archivo:", e)
        return ""

    def write_file_b(self, content):
        try:
            with open(os.path.join(self.root, self.filename+".slo"), 'wb') as file:
                file.write(bytes(content))
        except OSError or FileNotFoundError as e:
            print("Error al escribir en el archivo:", e)
