# Generar Instalador


### Forma con un Ventana

```bash
pyinstaller --name=WinSLO --add-data "banner.png;." --add-data "icon.ico;." --icon=icon.ico  --version-file=version_info.rc --windowed --add-data "Graphviz/bin/*;." WinSLO.py
```
### Forma con un Terminal

```bash
pyinstaller --name=WinSLO --add-data "banner.png;." --add-data "icon.ico;."  --icon=icon.ico --version-file=version_info.rc --console --add-data "Graphviz/bin/*;."  WinSLO.py
```



