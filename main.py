from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from datetime import date
import sys
from mysql_database import Database

db = Database()


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Main Window")
        self.initUi()

    def initUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Im a label")
        self.label.move(50, 50)


        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.move(100,100)
        self.lineEdit.returnPressed.connect(self.pressed)

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.move(100, 150)
        self.lineEdit2.returnPressed.connect(self.pressed)

        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit3.move(100, 200)
        self.lineEdit3.returnPressed.connect(self.pressed)

        self.lineEdit4 = QtWidgets.QLineEdit(self)
        self.lineEdit4.move(100, 250)
        self.lineEdit4.returnPressed.connect(self.pressed)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.get_results)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

    def pressed(self):
        self.label.setText(self.lineEdit.text())
        self.update()

    def get_results(self):
        results = [self.lineEdit.text(),self.lineEdit2.text(),self.lineEdit3.text(),self.lineEdit4.text()]
        print(db.get_active_trip())
        for result in results:
            print(result)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()