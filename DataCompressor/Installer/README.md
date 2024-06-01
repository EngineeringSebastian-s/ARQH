# Generar Instalador


### Forma con un Ventana

```bash
pyinstaller --name=WinSLO --add-data "banner.png;." --add-data "icon.ico;." --icon=icon.ico  --version-file=version_info.rc --windowed --add-data "Graphviz/bin/*;." WinSLO.py
```
### Forma con un Terminal

```bash
pyinstaller --name=WinSLO --add-data "banner.png;." --add-data "icon.ico;."  --icon=icon.ico --version-file=version_info.rc --console --add-data "Graphviz/bin/*;."  WinSLO.py
```


## Título de la Licencia
#### Licencia del Proyecto WinSLO

## Texto de la Licencia
El siguiente texto explica que WinSLO es un desarrollo de Sebastián López Osorno, un proyecto académico sin ánimo de lucro para la materia de Arquitectura de Hardware del Politécnico Jaime Isaza Cadavid de Medellín.

## Título de la Instalación
#### Instalador de Compresor de Datos WinSLO

## Texto de la Instalación
Bienvenido al Instalador de WinSLO
Gracias por instalar WinSLO.
WinSLO es un software desarrollado por Sebastián López Osorno como parte de un proyecto académico para la materia de Arquitectura de Hardware en el Politécnico Jaime Isaza Cadavid de Medellín. Este software no tiene fines de lucro y está diseñado para ayudar en la compresión y descompresión de archivos utilizando el algoritmo de Huffman.
Siga las instrucciones en pantalla para completar la instalación.
