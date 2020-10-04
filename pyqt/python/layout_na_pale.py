import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
	QLabel, QPushButton, QLineEdit)

if __name__ == '__main__':
	app = QApplication([])
	window = QMainWindow()
	window.setGeometry(200, 200, 300, 500)
	window.setWindowTitle('Bieda w ch*j')

	label = QLabel('Labelka', window)
	label.move(100, 50)

	button = QPushButton('Przycisk', window)
	button.move(150, 90)

	edit = QLineEdit(window)
	edit.setText('Text area')
	edit.move(30, 200)
	edit.resize(140, 300)

	window.show()
	sys.exit(app.exec())
