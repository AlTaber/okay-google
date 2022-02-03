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
        self.image = QLabel(self)
        self.reloadMap()

    def reloadMap(self, coords='19.9026511,54.6432638'):  # 19.9026511,54.6432638
        self.image.clear()
        data = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn=0.1,0.1&l=sat').content
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        self.image.move(5, 100)
        self.image.resize(500, 350)
        self.image.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.set_img)

    def set_img(self):
        print(self.lineEdit.text())
        self.reloadMap(self.lineEdit.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Searcher()
    ex.show()
    sys.exit(app.exec())
