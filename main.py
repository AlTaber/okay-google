from debil import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
import sys
import requests


class Searcher(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        data = requests.get('https://static-maps.yandex.ru/1.x/?ll=19.9026511,54.6432638&spn=0.1,0.1&l=sat').content
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        self.image = QLabel(self)
        self.image.move(5, 100)
        self.image.resize(500, 350)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Searcher()
    ex.show()
    sys.exit(app.exec())
