from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from datetime import date
from PyQt5.uic import loadUi
import sys
from database import client_controller,cost_controller,transaction_controller,trip_controller,products_controller


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.nd = NewDialog()
        loadUi("main_window.ui", self)
        self.box_transac_client.addItems(client_controller.get_clients_list())
        self.tr_box_sale_client.addItems(client_controller.get_clients_list())
        self.button_transac_add.clicked.connect(self.transactionForms)
        self.update_products()
        self.update_types()
        self.tr_start_trip_button.clicked.connect(self.start_trip)
        self.tr_finish_trip_button.clicked.connect(self.finish_trip)
        self.tr_add_cost.clicked.connect(self.add_cost)
        self.tr_button_sale.clicked.connect(self.saleForms)
        self.button_products_add.clicked.connect(self.add_productForms)
        self.button_products_add_type.clicked.connect(self.add_typeForms)
        self.button_products_remove.clicked.connect(self.remove_productForms)
        self.button_products_remove_type.clicked.connect(self.remove_typeForms)

    def clientForms(self):
        if client_controller.insert_client((self.input_clients_name.text(), self.input_clients_phone.text(),
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
        self.box_transac_client.addItems(client_controller.get_clients_list())

    def transactionForms(self):
        sale_date = self.input_transac_pay_day.text().split("/")
        sale_date = date(int(sale_date[2]), int(sale_date[1]), int(sale_date[0]))

        transaction_controller.insert_transaction(self.box_transac_client.currentText(),
                              [self.box_transac_product.currentText(), float(self.input_transac_purchase.text()),
                               float(self.input_transac_sale.text()), sale_date.__str__(),
                               int(self.input_transac_quantity.text()), self.box_transac_payment.currentText(),
                               self.box_transact_type.currentText()], 0)

    def saleForms(self):
        sale_date = self.tr_input_sale_pay_day.text().split("/")
        sale_date = date(int(sale_date[2]), int(sale_date[1]), int(sale_date[0]))
        # transaction_controller.insert_transaction(self.tr_box_sale_client.currentText(),
        #                       [self.tr_box_sale_product.currentText(), float(self.tr_input_sale_pruchase.text()),
        #                        float(self.tr_input_sale_value.text()), sale_date.__str__(),
        #                        int(self.tr_input_sale_quantity.text()), self.tr_box_sale_payment.currentText(),
        #                        self.tr_box_sale_type.currentText()], 1)

        print(self.tr_box_sale_client.currentText(),
                  [self.tr_box_sale_product.currentText(),
                   float(self.tr_input_sale_purchase.text()),
                   float(self.tr_input_sale_value.text()), sale_date.__str__(),
                   int(self.tr_input_sale_quantity.text()),
                   self.tr_box_sale_payment.currentText(),
                   self.tr_box_sale_type.currentText()], 1)

    def add_productForms(self):
        if products_controller.insert_product(self.input_products_add_name.text()):
            self.display_success_alert("Produto adicionado com sucesso")
            self.update_products()
        else:
            self.display_error_alert("Já existe um produto com esse nome")
        self.input_products_add_name.clear()

    def remove_productForms(self):
        if products_controller.delete_product(self.input_products_remove_name.text()):
            self.display_success_alert("Produto removido com sucesso")
            self.update_products()
        else:
            self.display_error_alert("Não um produto com esse nome")
        self.input_products_remove_name.clear()

    def add_typeForms(self):
        if products_controller.insert_type(self.input_products_add_name_type.text()):
            self.display_success_alert("Tipo adicionado com sucesso")
            self.update_types()
        else:
            self.display_error_alert("Já existe um tipo com esse nome")
        self.input_products_add_name_type.clear()

    def remove_typeForms(self):
        if products_controller.delete_type(self.input_products_remove_name_type.text()):
            self.display_success_alert("Tipo removido com sucesso")
            self.update_types()
        else:
            self.display_error_alert("Não um tipo com esse nome")
        self.input_products_remove_name_type.clear()


    def update_products(self):
        self.tr_box_sale_product.clear()
        self.tr_box_sale_product.addItems(products_controller.get_products_list())
        self.box_transac_product.clear()
        self.box_transac_product.addItems(products_controller.get_products_list())

    def update_types(self):
        self.box_transac_type.clear()
        self.box_transac_type.addItems(products_controller.get_types_list())
        self.tr_box_sale_type.clear()
        self.tr_box_sale_type.addItems(products_controller.get_types_list())



    def start_trip(self):
        self.nd.show()
        self.nd.pushButton.clicked.connect(self.get_trip_forms)

    def display_success_alert(self, message):
        success_message = QtWidgets.QMessageBox()
        success_message.setIcon(QtWidgets.QMessageBox.Information)
        success_message.setText(message)
        success_message.setWindowTitle("Sucesso")
        success_message.addButton(QtWidgets.QMessageBox.Ok)
        success_message.exec_()

    def display_error_alert(self, message):
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setText(message)
        error_message.setWindowTitle("Erro")
        error_message.addButton(QtWidgets.QMessageBox.Ok)
        error_message.exec_()

    def get_trip_forms(self):
        if trip_controller.start_trip(
                (date.today().__str__(), 1, 0, 0, 0, self.nd.tr_input_origin.text(), self.nd.tr_input_destiny.text())):
            self.display_success_alert("Viagem iniciada com sucesso!")
        else:
            self.display_error_alert("Não é possível iniciar uma viagem sem finalizar a atual")
        self.nd.tr_input_origin.clear()
        self.nd.tr_input_destiny.clear()
        self.nd.close()

    def finish_trip(self):
        if trip_controller.end_trip(date.today().__str__()):
            self.display_success_alert("Viagem finalizada com sucesso")
        else:
            self.display_error_alert("Não é possível finalizar uma viagem sem inicia-la primeiro")

    def add_cost(self):
        if cost_controller.insert_cost([self.tr_box_cost_type.currentText(),float(self.tr_input_cost_value.text()),self.tr_input_cost_description.text()]):
            self.display_success_alert("Custo adicionado à viagem!")
        else:
            self.display_error_alert("Não é possível adicionar um custo sem uma viagem inicializada")

class NewDialog(QDialog):
    def __init__(self):
        super(NewDialog, self).__init__()
        loadUi("start_trip.ui", self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainWindow = MainWindow()
widget.addWidget(mainWindow)
widget.setFixedWidth(900)
widget.setFixedHeight(550)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
