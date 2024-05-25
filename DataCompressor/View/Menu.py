import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox

from Logic import Compressor as Cm


class TextLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Suelta el archivo de texto aquí \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa;PO
                padding: 10px;
                word-wrap: break-word;
            }
        ''')
        self.setWordWrap(True)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.textViewer = TextLabel()
        mainLayout.addWidget(self.textViewer)

        self.actionButton = QPushButton("Comprimir/Descomprimir", self)
        self.actionButton.setEnabled(False)
        self.actionButton.clicked.connect(self.performAction)
        mainLayout.addWidget(self.actionButton)

        self.setLayout(mainLayout)

        self.filePath = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and (urls[0].toLocalFile().endswith('.txt') or urls[0].toLocalFile().endswith('.slo')):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and (urls[0].toLocalFile().endswith('.txt') or urls[0].toLocalFile().endswith('.slo')):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and (urls[0].toLocalFile().endswith('.txt') or urls[0].toLocalFile().endswith('.slo')):
                event.setDropAction(Qt.CopyAction)
                self.filePath = urls[0].toLocalFile()
                try:
                    self.set_text(self.filePath)
                    self.updateButton()
                    event.accept()
                except Exception as e:
                    self.showAlert(f"Error al abrir el archivo: {e}")
                    event.ignore()
            else:
                event.ignore()
        else:
            event.ignore()

    def set_text(self, file_path):
        try:
            if file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    content = file.read()
            elif file_path.endswith('.slo'):
                with open(file_path, 'rb') as file:
                    content = file.read()
                content = content.decode('utf-8', errors='ignore')  # Decodificar si es necesario
            self.textViewer.setText(content)
        except Exception as e:
            raise e

    def updateButton(self):
        if self.filePath.endswith('.txt'):
            self.actionButton.setText("Comprimir")
        elif self.filePath.endswith('.slo'):
            self.actionButton.setText("Descomprimir")
        self.actionButton.setEnabled(True)

    def showAlert(self, message, title="Alerta"):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def performAction(self):
        if self.filePath.endswith('.txt'):
            self.compress()
        elif self.filePath.endswith('.slo'):
            self.decompress()

    def compress(self):
        try:
            file_dir = os.path.dirname(self.filePath)
            file_root, file_ext = os.path.splitext(self.filePath)
            file_name = os.path.basename(file_root)
            cm = Cm.Compressor()
            cm.Compress(file_name, file_dir)
            QMessageBox.information(self, "Acción",
                                    f"Archivo '{file_name}{file_ext}' comprimido con éxito en: {file_dir}")
        except Exception as e:
            self.showAlert(f"Error al comprimir el archivo '{file_name}{file_ext}': {e}")

    def decompress(self):
        try:
            file_dir = os.path.dirname(self.filePath)
            file_root, file_ext = os.path.splitext(self.filePath)
            file_name = os.path.basename(file_root)
            cm = Cm.Compressor()
            cm.Descompress(file_name, file_dir)
            QMessageBox.information(self, "Acción",
                                    f"Archivo '{file_name}{file_ext}' descomprimido con éxito en: {file_dir}")
        except Exception as e:
            self.showAlert(f"Error al descomprimir el archivo '{file_name}{file_ext}': {e}")
