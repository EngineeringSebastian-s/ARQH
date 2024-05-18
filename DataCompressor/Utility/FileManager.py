import os

class FileManager:
    def __init__(self, filename):
        self.root = os.getcwd()
        self.file_path = os.path.join(self.root, "Data", filename)

    def read_file(self, ext):
        try:
            with open(self.file_path + ext, "r", encoding='utf-8') as file:
                return file.read()
        except OSError or FileNotFoundError as e:
            print("Error al leer el archivo:", e)
        return ""

    def write_file(self, content, ext):
        try:
            with open(self.file_path + ext, 'w', encoding='utf-8') as file:
                file.write(content)
        except OSError or FileNotFoundError as e:
            print("Error al escribir en el archivo:", e)

    def create_file(self, ext):
        try:
            with open(self.file_path+ext, 'x') as f:
                print(f"Archivo creado exitosamente.")
        except FileExistsError:
            print("El archivo ya existe")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def read_file_b(self, ext):
        try:
            with open(self.file_path + ext, "rb") as file:
                return file.read()
        except OSError or FileNotFoundError as e:
            print("Error al leer el archivo:", e)
        return ""

    def write_file_b(self, content, ext):
        try:
            with open(self.file_path + ext, 'wb') as file:
                file.write(content)
        except OSError or FileNotFoundError as e:
            print("Error al escribir en el archivo:", e)
