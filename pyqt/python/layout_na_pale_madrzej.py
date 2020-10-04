import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
	QLabel, QPushButton, QLineEdit)


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle('Bieda w ch*j')
		self.setGeometry(200, 200, 300, 500)

		label = QLabel('Labelka', self)
		label.move(100, 50)

		button = QPushButton('Przycisk', self)
		button.move(150, 90)

		edit = QLineEdit(self)
		edit.setText('Text area')
		edit.move(30, 200)
		edit.resize(140, 300)


if __name__ == '__main__':
	app = QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
