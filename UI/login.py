from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from main_dashboard import MainDashboard  # Make sure this file and class exist

import sys
import mysql.connector


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Login")
        self.setGeometry(100, 100, 300, 200)

        # Create widgets
        self.label_username = QLabel("Username:")
        self.input_username = QLineEdit()
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton("Login")
        self.button_login.clicked.connect(self.handle_login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1603",
                database="db"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM operators WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()

            if result:
                QMessageBox.information(self, "Success", f"Welcome, {username}!")
                self.hide()  # Hide login window
                self.dashboard = MainDashboard()  # Launch main dashboard
                self.dashboard.show()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Database error:\n{err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
