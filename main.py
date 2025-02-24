import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from addEditCoffeeForm import Ui_AddEditCoffeeForm
from maind import Ui_MainWindow

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
