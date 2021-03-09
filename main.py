from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from datetime import date
from PyQt5.uic import loadUi
import sys
from mysql_database import Database
from create_trip_window import Ui_OtherWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.nd = NewDialog()
        loadUi("main_window.ui", self)
        self.box_transac_client.addItems(db.get_clients_list())
        self.tr_box_sale_client.addItems(db.get_clients_list())
        self.tr_start_trip_button.clicked.connect(self.start_trip)
        self.tr_finish_trip_button.clicked.connect(self.finish_trip)
        # self.pushButton.clicked.connect(self.go_to_second_window)

    # def go_to_second_window(self):
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    def clientForms(self):
        if db.insert_client((self.input_clients_name.text(), self.input_clients_phone.text(),
                             self.input_clients_address.text(), self.input_clients_company.text(),
                             self.input_clients_email.text())):
            self.display_success_alert("Cliente criado com sucesso!")
        else:
            self.display_error_alert("Já existe um cliente com esse nome")
        self.input_clients_name.clear()
        self.input_clients_phone.clear()
        self.input_clients_address.clear()
        self.input_clients_company.clear()
        self.input_clients_email.clear()
        self.box_transac_client.clear()
        self.box_transac_client.addItems(db.get_clients_list())

    def transactionForms(self):
        sale_date = self.input_transac_pay_day.text().split("/")
        sale_date = date(int(sale_date[2]), int(sale_date[1]), int(sale_date[0]))

        db.insert_transaction(self.box_transac_client.currentText(),
                              [self.box_transac_product.currentText(), float(self.input_transac_purchase.text()),
                               float(self.input_transac_sale.text()), sale_date.__str__(),
                               int(self.input_transac_quantity.text()), self.box_transac_payment.currentText(),
                               self.box_transact_type.currentText()], 0)

    def start_trip(self):
        self.nd.show()
        self.nd.pushButton.clicked.connect(self.get_trip_forms)

    def display_success_alert(self,message):
        success_message = QtWidgets.QMessageBox()
        success_message.setIcon(QtWidgets.QMessageBox.Information)
        success_message.setText(message)
        success_message.setWindowTitle("Sucesso")
        success_message.addButton(QtWidgets.QMessageBox.Ok)
        success_message.exec_()

    def display_error_alert(self,message):
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setText(message)
        error_message.setWindowTitle("Erro")
        error_message.addButton(QtWidgets.QMessageBox.Ok)
        error_message.exec_()

    def get_trip_forms(self):
        if db.start_trip((date.today().__str__(), 1, 0, 0, 0, self.nd.tr_input_origin.text(), self.nd.tr_input_destiny.text())):
            self.display_success_alert("Viagem iniciada com sucesso!")
        else:
            self.display_error_alert("Não é possível iniciar uma viagem sem finalizar a atual")
        self.nd.tr_input_origin.clear()
        self.nd.tr_input_destiny.clear()
        self.nd.close()

    def finish_trip(self):
        if db.end_trip(date.today().__str__()):
            self.display_success_alert("Viagem finalizada com sucesso")
        else:
            self.display_error_alert("Não é possível finalizar uma viagem sem inicia-la primeiro")



class CreateTripWindow(QMainWindow):
    def __init__(self):
        super(CreateTripWindow, self).__init__()
        loadUi("create_trip_window.ui", self)


class NewDialog(QDialog):
    def __init__(self):
        super(NewDialog, self).__init__()
        loadUi("test2.ui",self)


db = Database()
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainWindow = MainWindow()
createTripWindow = CreateTripWindow()
widget.addWidget(mainWindow)
widget.addWidget(createTripWindow)
widget.setFixedWidth(900)
widget.setFixedHeight(550)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
