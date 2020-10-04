import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox, QVBoxLayout,
                             QLineEdit, QPushButton, QWidget, QHBoxLayout)


class SuperCheckbox(QHBoxLayout):
    def __init__(self, parent=None):
        super(SuperCheckbox, self).__init__(parent)

        self.checkbox = QCheckBox()
        self.addWidget(self.checkbox)

        self.edit = QLineEdit()
        self.edit.setText('Placeholder')
        self.addWidget(self.edit)

        button = QPushButton()
        button.setIcon(QIcon('icons/plus.svg'))
        button.clicked.connect(self.removeThis)
        button.resize(self.sizeHint())
        self.addWidget(button)

    def checkState(self):
        return self.checkbox.checkState()

    def removeThis(self):
        print('Removed !')


class CentralWidget(QWidget):
    items = []

    def __init__(self, parent):
        super(CentralWidget, self).__init__(parent)
        self.container = QVBoxLayout(self)

        btn = QPushButton('Dodaj')
        btn.clicked.connect(self.addSuperCheckbox)
        btn.resize(btn.sizeHint())
        self.container.addWidget(btn)

    def addSuperCheckbox(self):
        item = SuperCheckbox()
        self.container.addLayout(item)
        self.items.append(item)


class GlowneOkienko(QMainWindow):
    def __init__(self):
        super(GlowneOkienko, self).__init__(None)

        self.setWindowTitle('Dynamic layout & typ złożony')
        self.setWindowIcon(QIcon('icons/exit.svg'))
        self.setGeometry(500, 400, 600, 400)

        self.widget = CentralWidget(self)
        self.setCentralWidget(self.widget)


if __name__ == '__main__':

    app = QApplication([])
    window = GlowneOkienko()
    window.show()

    sys.exit(app.exec_())

