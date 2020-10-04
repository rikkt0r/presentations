import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGroupBox, QVBoxLayout, QGridLayout, QMainWindow, QAction


class GridWidget(QWidget):
    def __init__(self):
        super(GridWidget, self).__init__()
        self.container = QVBoxLayout()
        self.setLayout(self.container)

        self.setUpGrid()
        self.container.addWidget(self.hGroupBox)

    def setUpGrid(self):
        self.hGroupBox = QGroupBox("Grid example")

        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        # QGridLayout::addWidget(elem, y, x, (opt)y_size, (opt)x_size)

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2(2)'), 0, 1, 1, 2)
        # layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4(3)'), 1, 0, 1, 3)
        # layout.addWidget(QPushButton('5'), 1, 1)
        # layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.hGroupBox.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.grid = GridWidget()
        self.setCentralWidget(self.grid)
        self.initMenu()

    def initMenu(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')

        exit = QAction(QIcon('images/icons/exit.svg'), '&Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        exit.triggered.connect(self.close)
        fileMenu.addAction(exit)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

