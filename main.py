import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox

class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.load()

    def load(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        conn.close()

    def add(self):
        dialog = AddEditCoffeeForm()
        if dialog.exec():
            self.load()

    def edit(self):
        selected_items = self.tableWidget.selectedItems()
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
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.coffee_id = coffee_id
        self.saveButton.clicked.connect(self.save)
        self.cancelButton.clicked.connect(self.close)
        if self.coffee_id:
            self.load_coffee_data()

    def load_coffee_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee WHERE id = ?", (self.coffee_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            self.idLineEdit.setText(str(row[0]))
            self.nameLineEdit.setText(row[1])
            self.roastLineEdit.setText(row[2])
            self.isGroundComboBox.setCurrentText("Зерна" if row[3] else "Молотый")
            self.descriptionLineEdit.setText(row[4])
            self.priceLineEdit.setText(str(row[5]))
            self.volumeLineEdit.setText(str(row[6]))

    def save(self):
        name = self.nameLineEdit.text()
        roast = self.roastLineEdit.text()
        is_ground = "Зерна" if self.isGroundComboBox.currentText() == "Зерна" else "Молотый"
        description = self.descriptionLineEdit.text()
        price = self.priceLineEdit.text()
        volume = self.volumeLineEdit.text()
        conn = sqlite3.connect('coffee.sqlite')
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
