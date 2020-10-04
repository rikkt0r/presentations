import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

if __name__ == '__main__':
	app = QApplication([])
	window = QMainWindow()
	window.setWindowTitle('Pierwszy apku')
	QLabel('Labelka', window)
	window.show()
	sys.exit(app.exec())
