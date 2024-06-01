import os
import sys

# Ruta al directorio raíz donde se ejecuta el archivo
root_path = os.path.abspath(os.path.dirname(sys.argv[0]))

# Agregar la carpeta raíz al PATH del sistema
os.environ['PATH'] = root_path + os.pathsep + os.environ.get('PATH', '')
