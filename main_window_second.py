# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 771, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 721, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 211, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 120, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 67, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 150, 211, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 180, 211, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 210, 211, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 67, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 240, 211, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(190, 290, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(170, 60, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(80, 60, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(70, 110, 67, 17))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 110, 86, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 160, 211, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 200, 211, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(170, 240, 211, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(170, 280, 211, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(40, 160, 121, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(40, 200, 111, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(20, 240, 141, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(40, 280, 91, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(10, 320, 151, 17))
        self.label_13.setObjectName("label_13")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 320, 86, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 370, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(280, 110, 67, 17))
        self.label_8.setObjectName("label_8")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(320, 110, 86, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(80, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(450, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.line = QtWidgets.QFrame(self.tab_4)
        self.line.setGeometry(QtCore.QRect(360, 60, 20, 331))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(20, 130, 51, 17))
        self.label_16.setObjectName("label_16")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 130, 211, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 200, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 200, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(420, 130, 51, 17))
        self.label_17.setObjectName("label_17")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 130, 211, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 10, 711, 411))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableView = QtWidgets.QTableView(self.tab_6)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 411, 192))
        self.tableView.setObjectName("tableView")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(20, 240, 91, 17))
        self.label_18.setObjectName("label_18")
        self.start_trip_button = QtWidgets.QPushButton(self.tab_6)
        self.start_trip_button.setGeometry(QtCore.QRect(470, 50, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_trip_button.setFont(font)
        self.start_trip_button.setObjectName("start_trip_button")
        self.finish_trip_button = QtWidgets.QPushButton(self.tab_6)
        self.finish_trip_button.setGeometry(QtCore.QRect(470, 240, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.finish_trip_button.setFont(font)
        self.finish_trip_button.setObjectName("finish_trip_button")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_37 = QtWidgets.QLabel(self.tab_7)
        self.label_37.setGeometry(QtCore.QRect(30, 20, 67, 17))
        self.label_37.setObjectName("label_37")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_9.setGeometry(QtCore.QRect(120, 20, 86, 25))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_10.setGeometry(QtCore.QRect(120, 70, 86, 25))
        self.comboBox_10.setObjectName("comboBox_10")
        self.label_38 = QtWidgets.QLabel(self.tab_7)
        self.label_38.setGeometry(QtCore.QRect(20, 70, 67, 17))
        self.label_38.setObjectName("label_38")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_11.setGeometry(QtCore.QRect(280, 70, 86, 25))
        self.comboBox_11.setObjectName("comboBox_11")
        self.label_39 = QtWidgets.QLabel(self.tab_7)
        self.label_39.setGeometry(QtCore.QRect(240, 70, 67, 17))
        self.label_39.setObjectName("label_39")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_45.setGeometry(QtCore.QRect(180, 120, 211, 21))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_82 = QtWidgets.QLabel(self.tab_7)
        self.label_82.setGeometry(QtCore.QRect(10, 120, 121, 17))
        self.label_82.setObjectName("label_82")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_46.setGeometry(QtCore.QRect(180, 160, 211, 21))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_83 = QtWidgets.QLabel(self.tab_7)
        self.label_83.setGeometry(QtCore.QRect(10, 160, 111, 17))
        self.label_83.setObjectName("label_83")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_60.setGeometry(QtCore.QRect(180, 200, 211, 21))
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.label_107 = QtWidgets.QLabel(self.tab_7)
        self.label_107.setGeometry(QtCore.QRect(10, 190, 141, 17))
        self.label_107.setObjectName("label_107")
        self.label_132 = QtWidgets.QLabel(self.tab_7)
        self.label_132.setGeometry(QtCore.QRect(10, 230, 91, 17))
        self.label_132.setObjectName("label_132")
        self.lineEdit_75 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_75.setGeometry(QtCore.QRect(180, 240, 211, 21))
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.comboBox_40 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_40.setGeometry(QtCore.QRect(160, 290, 86, 25))
        self.comboBox_40.setObjectName("comboBox_40")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_25.setGeometry(QtCore.QRect(160, 340, 89, 25))
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_133 = QtWidgets.QLabel(self.tab_7)
        self.label_133.setGeometry(QtCore.QRect(0, 290, 151, 17))
        self.label_133.setObjectName("label_133")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_134 = QtWidgets.QLabel(self.tab_8)
        self.label_134.setGeometry(QtCore.QRect(40, 70, 41, 17))
        self.label_134.setObjectName("label_134")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_26.setGeometry(QtCore.QRect(90, 230, 89, 25))
        self.pushButton_26.setObjectName("pushButton_26")
        self.comboBox_41 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_41.setGeometry(QtCore.QRect(170, 70, 121, 25))
        self.comboBox_41.setObjectName("comboBox_41")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.lineEdit_76 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_76.setGeometry(QtCore.QRect(170, 110, 211, 21))
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.label_135 = QtWidgets.QLabel(self.tab_8)
        self.label_135.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.label_135.setObjectName("label_135")
        self.label_136 = QtWidgets.QLabel(self.tab_8)
        self.label_136.setGeometry(QtCore.QRect(10, 150, 141, 17))
        self.label_136.setObjectName("label_136")
        self.lineEdit_77 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_77.setGeometry(QtCore.QRect(170, 150, 211, 21))
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Visão Geral"))
        self.label.setText(_translate("MainWindow", "Nome"))
        self.label_2.setText(_translate("MainWindow", "Telefone"))
        self.label_3.setText(_translate("MainWindow", "Endereço"))
        self.label_4.setText(_translate("MainWindow", "Empresa"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Clientes"))
        self.label_6.setText(_translate("MainWindow", "Cliente"))
        self.label_7.setText(_translate("MainWindow", "Produto"))
        self.label_9.setText(_translate("MainWindow", "Valor de Compra"))
        self.label_10.setText(_translate("MainWindow", "Valor de Venda"))
        self.label_11.setText(_translate("MainWindow", "Data de pagamento"))
        self.label_12.setText(_translate("MainWindow", "Quantidade "))
        self.label_13.setText(_translate("MainWindow", "Forma de pagamento"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.label_8.setText(_translate("MainWindow", "Tipo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Transações"))
        self.label_14.setText(_translate("MainWindow", "Adicionar Produto"))
        self.label_15.setText(_translate("MainWindow", "Remover Produto"))
        self.label_16.setText(_translate("MainWindow", "Nome"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.pushButton_4.setText(_translate("MainWindow", "Remover"))
        self.label_17.setText(_translate("MainWindow", "Nome"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Produtos"))
        self.label_18.setText(_translate("MainWindow", "Custo Geral:"))
        self.start_trip_button.setText(_translate("MainWindow", "Começar Viagem"))
        self.finish_trip_button.setText(_translate("MainWindow", "Finalizar Viagem"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Visão da Viagem"))
        self.label_37.setText(_translate("MainWindow", "Cliente"))
        self.label_38.setText(_translate("MainWindow", "Produto"))
        self.label_39.setText(_translate("MainWindow", "Tipo"))
        self.label_82.setText(_translate("MainWindow", "Valor de Compra"))
        self.label_83.setText(_translate("MainWindow", "Valor de Venda"))
        self.label_107.setText(_translate("MainWindow", "Data de pagamento"))
        self.label_132.setText(_translate("MainWindow", "Quantidade "))
        self.pushButton_25.setText(_translate("MainWindow", "Submit"))
        self.label_133.setText(_translate("MainWindow", "Forma de pagamento"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Vendas"))
        self.label_134.setText(_translate("MainWindow", "Tipo"))
        self.pushButton_26.setText(_translate("MainWindow", "Submit"))
        self.comboBox_41.setItemText(0, _translate("MainWindow", "Alimentação"))
        self.comboBox_41.setItemText(1, _translate("MainWindow", "Combustível"))
        self.comboBox_41.setItemText(2, _translate("MainWindow", "Mecânico"))
        self.comboBox_41.setItemText(3, _translate("MainWindow", "Estadia"))
        self.comboBox_41.setItemText(4, _translate("MainWindow", "Outros"))
        self.label_135.setText(_translate("MainWindow", "Valor do Custo"))
        self.label_136.setText(_translate("MainWindow", "Descrição (Opcional)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Custo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Viagem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
