import sys

from PyQt5.QtWidgets import QApplication

from View import Menu as Mn

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Mn.Application()
    frame.show()
    sys.exit(app.exec_())
