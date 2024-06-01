# Generar Instalador


### Forma con un Ventana

```bash
pyinstaller --name=WinSLO --add-data "banner.png;." --icon=icon.ico  --version-file=version_info.rc --windowed --clean --add-data "Graphviz\bin" WinSLO.py
```
### Forma con un Terminal

```bash
pyinstaller --name=WinSLO --add-data "banner.png;." --icon=icon.ico --version-file=version_info.rc --onefile --console --clean --add-data "Graphviz\bin"  WinSLO.py
```



