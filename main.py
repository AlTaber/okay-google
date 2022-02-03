from debil import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
import sys


class Searcher(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def initUi(self):
        self.pixmap = QPixmap("путь до изображения")

        self.image = QLabel(self)
        self.image.move(5, 100)
        self.image.resize(650, 450)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Searcher()
    ex.show()
    sys.exit(app.exec())
