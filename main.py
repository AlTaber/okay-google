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
        self.obj = ''
        self.coords = [19.9026511, 54.6432638]
        self.map_format = "sat"
        self.spn = 0.1
        self.reloadMap()

        self.radioButton.toggled.connect(self.change_map_format)
        self.radioButton_2.toggled.connect(self.change_map_format)
        self.radioButton_3.toggled.connect(self.change_map_format)
        self.pushButton.clicked.connect(self.search)

    def reloadMap(self):  # 19.9026511,54.6432638
        self.image.clear()
        data = requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={self.coords}&spn=0.1,0.1&l={self.map_format}').content

    def reloadMap(self):  # 19.9026511,54.6432638
        self.image.clear()
        self.lineEdit.setText(f'{self.coords[0]}, {self.coords[1]}')
        data = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={self.coords[0]},{self.coords[1]}&spn={self.spn},{self.spn}&l={self.map_format}').content
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        self.image.move(5, 100)
        self.image.resize(500, 350)
        self.image.setPixmap(self.pixmap)
#<<<<<<< AndrDD
#=======
        self.pushButton.clicked.connect(self.set_img)

    def set_img(self):
        print(self.lineEdit.text())
        self.coords = [float(el) for el in self.lineEdit.text().split(', ')]
        self.reloadMap()
#>>>>>>> saks

    def change_map_format(self):
        if self.sender().text() == "Спутник":
            self.map_format = "sat"
        elif self.sender().text() == "Схема":
            self.map_format = "map"
        elif self.sender().text() == "Гибрид":
            self.map_format = "sat,skl"
        self.reloadMap()

    def search(self):
        self.obj = self.lineEdit.text()
        toponym_to_find = self.obj
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_a, toponym_b = toponym_coodrinates.split(" ")
        self.coords = f'{toponym_a},{toponym_b}'
        print(toponym_coodrinates)
        try:
            self.reloadMap()
        except:
            print('error')

    def move(self, direction=0):
        if not direction:
            self.coords[0] -= self.spn
        elif direction == 1:
            self.coords[0] += self.spn
        elif direction == 2:
            self.coords[1] -= self.spn
        elif direction == 3:
            self.coords[1] += self.spn
        self.reloadMap()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.spn += 0.1
            self.reloadMap()
        elif event.key() == Qt.Key_PageDown:
            self.spn = 0.1 if self.spn - 0.05 <= 0.1 else self.spn - 0.05
            self.reloadMap()

        elif event.key() == Qt.Key_Up:
            self.move(3)
        elif event.key() == Qt.Key_Down:
            self.move(2)
        elif event.key() == Qt.Key_Left:
            self.move()
        elif event.key() == Qt.Key_Right:
            self.move(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Searcher()
    ex.show()
    sys.exit(app.exec())
