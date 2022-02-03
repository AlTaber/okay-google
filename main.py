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
        self.coords = '19.9026511,54.6432638'
        self.map_format = "sat"
        self.reloadMap()
        self.lineEdit.setText(self.coords)

        self.radioButton.toggled.connect(self.change_map_format)
        self.radioButton_2.toggled.connect(self.change_map_format)
        self.radioButton_3.toggled.connect(self.change_map_format)

    def reloadMap(self):  # 19.9026511,54.6432638
        self.image.clear()
        data = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={self.coords}&spn=0.1,0.1&l={self.map_format}').content
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        self.image.move(5, 100)
        self.image.resize(500, 350)
        self.image.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.set_img)

    def set_img(self):
        print(self.lineEdit.text())
        self.coords = self.lineEdit.text()
        self.reloadMap()

    def change_map_format(self):
        if self.sender().text() == "Спутник":
            self.map_format = "sat"
        elif self.sender().text() == "Схема":
            self.map_format = "map"
        elif self.sender().text() == "Гибрид":
            self.map_format = "sat,skl"
        self.reloadMap()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Searcher()
    ex.show()
    sys.exit(app.exec())
