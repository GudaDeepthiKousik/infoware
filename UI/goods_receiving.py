from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
)
import sys
import mysql.connector


class GoodsReceivingForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goods Receiving")
        self.setGeometry(100, 100, 400, 400)

        # Create form fields
        self.product_id_input = QLineEdit()
        self.supplier_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.rate_input = QLineEdit()
        self.tax_input = QLineEdit()

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)

        # Layout
        layout = QVBoxLayout()

        layout.addLayout(self._form_row("Product ID:", self.product_id_input))
        layout.addLayout(self._form_row("Supplier Details:", self.supplier_input))
        layout.addLayout(self._form_row("Quantity:", self.quantity_input))
        layout.addLayout(self._form_row("Unit:", self.unit_input))
        layout.addLayout(self._form_row("Rate per Unit:", self.rate_input))
        layout.addLayout(self._form_row("Tax:", self.tax_input))

        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def _form_row(self, label_text, widget):
        row = QHBoxLayout()
        row.addWidget(QLabel(label_text))
        row.addWidget(widget)
        return row

    def submit_form(self):
        try:
            product_id = self.product_id_input.text()
            supplier = self.supplier_input.text()
            quantity = float(self.quantity_input.text())
            unit = self.unit_input.text()
            rate = float(self.rate_input.text())
            tax = float(self.tax_input.text())

            total_rate = (quantity * rate) + tax

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1603",
                database="db"
            )
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO goods_receiving 
                (product_id, supplier_details, quantity, unit_of_measurement, rate_per_unit, total_rate, tax) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (product_id, supplier, quantity, unit, rate, total_rate, tax))

            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(self, "Success", "Goods record saved successfully!")

            self._clear_form()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n{e}")

    def _clear_form(self):
        self.product_id_input.clear()
        self.supplier_input.clear()
        self.quantity_input.clear()
        self.unit_input.clear()
        self.rate_input.clear()
        self.tax_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GoodsReceivingForm()
    window.show()
    sys.exit(app.exec())
