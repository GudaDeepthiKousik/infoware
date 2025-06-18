import os
import shutil
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout,
    QHBoxLayout, QPushButton, QFileDialog, QComboBox, QMessageBox
)


from PySide6.QtGui import QPixmap

class ProductMasterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master Form")

        self.layout = QVBoxLayout()

        self.barcode_input = self.add_field("Barcode:")
        self.sku_id_input = self.add_field("SKU ID:")
        self.category_input = self.add_field("Category:")
        self.subcategory_input = self.add_field("Subcategory:")
        self.product_name_input = self.add_field("Product Name:")
        self.description_input = self.add_field("Description:")

        self.tax_input = self.add_field("Tax:")
        self.price_input = self.add_field("Price:")

        self.unit_input = QComboBox()
        self.unit_input.addItems(["piece", "pack", "kg", "litre"])
        self.layout.addWidget(QLabel("Default Unit:"))
        self.layout.addWidget(self.unit_input)

        self.image_path = ""
        self.image_label = QLabel()
        self.layout.addWidget(QLabel("Product Image:"))
        self.select_image_btn = QPushButton("Select Image")
        self.select_image_btn.clicked.connect(self.select_image)
        self.layout.addWidget(self.select_image_btn)
        self.layout.addWidget(self.image_label)

        self.add_product_btn = QPushButton("Add Product")
        self.add_product_btn.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_product_btn)

        self.setLayout(self.layout)

    def add_field(self, label_text):
        label = QLabel(label_text)
        line_edit = QLineEdit()
        self.layout.addWidget(label)
        self.layout.addWidget(line_edit)
        return line_edit

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path).scaledToWidth(100)
            self.image_label.setPixmap(pixmap)

    def add_product(self):
        # Move image file to the project image folder
        image_folder = "product_images"
        os.makedirs(image_folder, exist_ok=True)

        image_filename = os.path.basename(self.image_path)
        dest_path = os.path.join(image_folder, image_filename)

        try:
            if self.image_path and self.image_path != dest_path:
                shutil.copy(self.image_path, dest_path)
        except shutil.SameFileError:
            pass  # File is already there

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1603",
                database="db"
            )
            cursor = conn.cursor()
             
            cursor.execute("USE `db`")

            query = """
            INSERT INTO `db`.`product_master_list`
            (barcode, sku_id, category, subcategory, product_image, product_name, description, tax, price, default_unit_of_measurement)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                self.barcode_input.text(),
                self.sku_id_input.text(),
                self.category_input.text(),
                self.subcategory_input.text(),
                dest_path,
                self.product_name_input.text(),
                self.description_input.text(),
                float(self.tax_input.text()),
                float(self.price_input.text()),
                self.unit_input.currentText()
            )

            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(self, "Success", "Product added successfully!")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

if __name__ == "__main__":
    app = QApplication([])
    window = ProductMasterForm()
    window.show()
    app.exec()