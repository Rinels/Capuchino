import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddEditCoffeeForm(object):
    def setupUi(self, AddEditCoffeeForm):
        AddEditCoffeeForm.setObjectName("AddEditCoffeeForm")
        AddEditCoffeeForm.resize(745, 454)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddEditCoffeeForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_id = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_id.setObjectName("label_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_id)
        self.idLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.idLineEdit.setReadOnly(True)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idLineEdit)
        self.label_name = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_name)
        self.nameLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameLineEdit)
        self.label_roast_degree = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_roast_degree.setObjectName("label_roast_degree")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_roast_degree)
        self.roastLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.roastLineEdit.setObjectName("roastLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.roastLineEdit)
        self.label_is_ground = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_is_ground.setObjectName("label_is_ground")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_is_ground)
        self.label_flavor_description = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_flavor_description.setObjectName("label_flavor_description")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_flavor_description)
        self.label_price = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_price.setObjectName("label_price")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_price)
        self.priceLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.priceLineEdit)
        self.label_package_volume = QtWidgets.QLabel(parent=AddEditCoffeeForm)
        self.label_package_volume.setObjectName("label_package_volume")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_package_volume)
        self.volumeLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.volumeLineEdit.setObjectName("volumeLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.volumeLineEdit)
        self.isGroundComboBox = QtWidgets.QComboBox(parent=AddEditCoffeeForm)
        self.isGroundComboBox.setObjectName("isGroundComboBox")
        self.isGroundComboBox.addItem("")
        self.isGroundComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.isGroundComboBox)
        self.descriptionLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descriptionLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.saveButton = QtWidgets.QPushButton(parent=AddEditCoffeeForm)
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        self.cancelButton = QtWidgets.QPushButton(parent=AddEditCoffeeForm)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(AddEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditCoffeeForm)

    def retranslateUi(self, AddEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditCoffeeForm.setWindowTitle(_translate("AddEditCoffeeForm", "Dialog"))
        self.label_id.setText(_translate("AddEditCoffeeForm", "ID:"))
        self.label_name.setText(_translate("AddEditCoffeeForm", "Название"))
        self.label_roast_degree.setText(_translate("AddEditCoffeeForm", "Степень обжарки"))
        self.label_is_ground.setText(_translate("AddEditCoffeeForm", "Молотый/Зерна"))
        self.label_flavor_description.setText(_translate("AddEditCoffeeForm", "Описание"))
        self.label_price.setText(_translate("AddEditCoffeeForm", "Цена"))
        self.label_package_volume.setText(_translate("AddEditCoffeeForm", "Объем упаковки"))
        self.isGroundComboBox.setItemText(0, _translate("AddEditCoffeeForm", "Зерна"))
        self.isGroundComboBox.setItemText(1, _translate("AddEditCoffeeForm", "Молотый"))
        self.saveButton.setText(_translate("AddEditCoffeeForm", "Сохранить"))
        self.cancelButton.setText(_translate("AddEditCoffeeForm", "Закрыть"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 771, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(50, 530, 75, 23))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(150, 530, 75, 23))
        self.editButton.setObjectName("editButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Степень обжарки"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Молотый/Зерна"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Объем упаковки"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Создаем экземпляр сгенерированного класса
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.add)
        self.ui.editButton.clicked.connect(self.edit)
        self.load()

    def load(self):
        conn = sqlite3.connect('data/coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        conn.close()

    def add(self):
        dialog = AddEditCoffeeForm()
        if dialog.exec():
            self.load()

    def edit(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Выберите запись для редактирования!")
            return
        coffee_id = int(selected_items[0].text())
        dialog = AddEditCoffeeForm(coffee_id)
        if dialog.exec():
            self.load()


class AddEditCoffeeForm(QDialog):
    def __init__(self, coffee_id = None):
        super().__init__()
        self.coffee_id = coffee_id
        self.ui = Ui_AddEditCoffeeForm()
        self.ui.setupUi(self)
        self.coffee_id = coffee_id
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.close)
        if self.coffee_id:
            self.load_coffee_data()

    def load_coffee_data(self):
        conn = sqlite3.connect('data/coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee WHERE id = ?", (self.coffee_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            self.ui.idLineEdit.setText(str(row[0]))
            self.ui.nameLineEdit.setText(row[1])
            self.ui.roastLineEdit.setText(row[2])
            self.ui.isGroundComboBox.setCurrentText("Зерна" if row[3] else "Молотый")
            self.ui.descriptionLineEdit.setText(row[4])
            self.ui.priceLineEdit.setText(str(row[5]))
            self.ui.volumeLineEdit.setText(str(row[6]))

    def save(self):
        name = self.ui.nameLineEdit.text()
        roast = self.ui.roastLineEdit.text()
        is_ground = "Зерна" if self.ui.isGroundComboBox.currentText() == "Зерна" else "Молотый"
        description = self.ui.descriptionLineEdit.text()
        price = self.ui.priceLineEdit.text()
        volume = self.ui.volumeLineEdit.text()
        conn = sqlite3.connect('data/coffee.sqlite')
        cursor = conn.cursor()
        if self.coffee_id:
            cursor.execute("""
                        UPDATE coffee
                        SET name = ?, roast_degree = ?, is_ground = ?, flavor_description = ?, price = ?, package_volume = ?
                        WHERE id = ?
                """, (name, roast, is_ground, description, price, volume, self.coffee_id))
        else:
            cursor.execute("""
                        INSERT INTO coffee (name, roast_degree, is_ground, flavor_description, price, package_volume)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (name, roast, is_ground, description, price, volume))
        conn.commit()
        self.accept()
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())