from debil import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import requests


class Searcher(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = QLabel(self)
        self.coords = '19.9026511,54.6432638'
        self.map_format = "sat"
        self.spn = 0.1
        self.reloadMap()

        self.radioButton.toggled.connect(self.change_map_format)
        self.radioButton_2.toggled.connect(self.change_map_format)
        self.radioButton_3.toggled.connect(self.change_map_format)

    def reloadMap(self):  # 19.9026511,54.6432638
        self.image.clear()
        data = requests.get(f'https://static-maps.yandex.'
                            f'ru/1.x/?ll={self.coords}&spn={self.spn},{self.spn}&l={self.map_format}').content
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.spn += 0.05
            self.reloadMap()
        elif event.key() == Qt.Key_Down:
            self.spn = 0.1 if self.spn - 0.05 <= 0.1 else self.spn - 0.05
            self.reloadMap()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Searcher()
    ex.show()
    sys.exit(app.exec())
