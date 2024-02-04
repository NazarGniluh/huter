import json

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from main import start_game

app = QApplication([])
settings = {}
window = QWidget()

def read_data():
    global settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)


def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file)



read_data()
print(settings)
start = QPushButton("ПОЧАТИ")
change = QPushButton("Change")
skin_1 = QLabel("КАРТИНКА")
skin_2 = QLabel("ПОкупка")
skin_2_img = QPixmap("bullet.png")
skin_2_img = skin_2_img.scaledToWidth(64)
skin_2.setPixmap(skin_2_img)
skin_1_img = QPixmap("asteroid.png")
skin_1_img = skin_1_img.scaledToWidth(64)
skin_1.setPixmap(skin_1_img)
skin_2_buy = QPushButton("КУПити айфон")
skin_1_buy = QPushButton("КУПИТИ СКІН")
line_edit = QLineEdit(settings["skin"])
linuz = QHBoxLayout()

linuz.addWidget(start)
linuz.addWidget(line_edit)
linuz.addWidget(change)
linuz.addWidget(skin_1)
linuz.addWidget(skin_2)
linuz.addWidget(skin_1_buy)
linuz.addWidget(skin_2_buy)
window.setLayout(linuz)

def buy_skin_1():
    if settings["money"] >= 7:
        settings["money"] -= 7
        settings["skin"] = "asteroid.png"
        write_data()
    else:
        print(" НЕ ХВАТАЄ ГРОШЕЙ!!")

def buy_skin_2():
    if settings["money"] >= 7:
        settings["money"] -= 7
        settings["skin"] = "bullet.png"
        write_data()
    else:
        print(" НЕ ХВАТАЄ ГРОШЕЙ!!")
def change_data():
    settings["skin"] = line_edit.text()
    write_data()

skin_2_buy.clicked.connect(buy_skin_2)
skin_1_buy.clicked.connect(buy_skin_1)
change.clicked.connect(change_data)
start.clicked.connect(start_game)

window.show()
app.exec()

