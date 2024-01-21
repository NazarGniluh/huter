import json

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
line_edit = QLineEdit(settings["skin"])
linuz = QHBoxLayout()

linuz.addWidget(start)
linuz.addWidget(line_edit)
linuz.addWidget(change)
window.setLayout(linuz)

def change_data():
    settings["skin"] = line_edit.text()
    write_data()

change.clicked.connect(change_data)
start.clicked.connect(start_game)

window.show()
app.exec()

