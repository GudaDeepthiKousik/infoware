from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys

# Updated imports
from product_master_list import ProductMasterForm
from goods_receiving import GoodsReceivingForm
from sales import SalesForm  # Changed from sales_form to sales


class MainDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management Dashboard")
        self.setFixedSize(400, 300)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # Heading label
        heading = QLabel("Welcome to Inventory Manager")
        heading.setFont(QFont("Arial", 14, QFont.Bold))
        heading.setStyleSheet("padding: 10px;")
        heading.setAlignment(Qt.AlignCenter)

        # Buttons
        self.product_master_btn = QPushButton("🗂️  Product Master List")
        self.goods_receiving_btn = QPushButton("📥  Goods Receiving")
        self.sales_btn = QPushButton("💸  Sales Form")

        for btn in [self.product_master_btn, self.goods_receiving_btn, self.sales_btn]:
            btn.setMinimumHeight(40)
            layout.addWidget(btn)

        layout.insertWidget(0, heading)
        central_widget.setLayout(layout)

        # Connect buttons
        self.product_master_btn.clicked.connect(self.open_product_master)
        self.goods_receiving_btn.clicked.connect(self.open_goods_receiving)
        self.sales_btn.clicked.connect(self.open_sales_form)

    def open_product_master(self):
        self.pm_form = ProductMasterForm()
        self.pm_form.show()

    def open_goods_receiving(self):
        self.gr_form = GoodsReceivingForm()
        self.gr_form.show()

    def open_sales_form(self):
        self.sales_form = SalesForm()
        self.sales_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainDashboard()
    window.show()
    sys.exit(app.exec())
