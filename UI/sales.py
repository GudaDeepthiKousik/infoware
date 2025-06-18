import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QPushButton, QVBoxLayout, QFormLayout, QMessageBox
)
import mysql.connector

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Form")

        # Form Layout
        layout = QFormLayout()

        self.product_id_input = QLineEdit()
        self.customer_details_input = QTextEdit()
        self.quantity_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.rate_input = QLineEdit()
        self.total_rate_input = QLineEdit()
        self.tax_input = QLineEdit()

        layout.addRow("Product ID:", self.product_id_input)
        layout.addRow("Customer Details:", self.customer_details_input)
        layout.addRow("Quantity:", self.quantity_input)
        layout.addRow("Unit of Measurement:", self.unit_input)
        layout.addRow("Rate per Unit:", self.rate_input)
        layout.addRow("Total Rate:", self.total_rate_input)
        layout.addRow("Tax:", self.tax_input)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.submit_data)
        layout.addRow(self.submit_btn)

        self.setLayout(layout)

    def submit_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1603",
                database="db"
            )
            cursor = conn.cursor()

            query = """
                INSERT INTO sales (
                    product_id, customer_details, quantity,
                    unit_of_measurement, rate_per_unit, total_rate, tax
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                int(self.product_id_input.text()),
                self.customer_details_input.toPlainText(),
                float(self.quantity_input.text()),
                self.unit_input.text(),
                float(self.rate_input.text()),
                float(self.total_rate_input.text()),
                float(self.tax_input.text())
            )

            cursor.execute(query, values)
            conn.commit()
            QMessageBox.information(self, "Success", "Sales entry saved.")

            # Clear fields
            self.product_id_input.clear()
            self.customer_details_input.clear()
            self.quantity_input.clear()
            self.unit_input.clear()
            self.rate_input.clear()
            self.total_rate_input.clear()
            self.tax_input.clear()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", str(e))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalesForm()
    window.show()
    sys.exit(app.exec())
