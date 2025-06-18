# Product Inventory Management System

This is a simple desktop application developed using **PySide6** and **MySQL**, designed for managing inventory operations through three key forms:

- **Goods Receiving**
- **Sales**
- **Product Master List**

Includes an **Operator Login** screen to authenticate users.

---

## 🚀 Features

1. **Login for Operators**

   - Secure login system for verified operators
   - Credentials stored in `operators` table in the database

2. **Goods Receiving Form**

   - Record supplier info, products, quantities, and tax
   - Calculates total rate and stores all data in the DB

3. **Sales Form**

   - Input customer purchase details
   - Product name, quantity, price, and tax
   - Stores transaction into the sales table

4. **Product Master List**

   - Maintain catalog with product images, SKU, barcode
   - Set default unit, tax, and base price

---

## 🛠️ Tech Stack

- **Frontend**: PySide6 (Python Qt Framework)
- **Backend**: MySQL
- **Packaging**: PyInstaller (for .exe file)

---

## 📂 Project Structure

```
infoware/
├── db/                           # SQL dump or data setup files
├── product_images/              # Product images used in master list
├── UI/
│   ├── goods_receiving.py
│   ├── login.py
│   ├── main_dashboard.py
│   ├── product_master_list.py
│   ├── sales.py
│   ├── build/                   # PyInstaller build output
│   └── dist/                    # Contains login.exe
├── virtualEnv/                  # Python virtual environment
├── README.md
```

---

## 🧪 Sample Credentials

| Username  | Password |
| --------- | -------- |
| operator1 | pass1    |
| operator2 | pass2    |

> Make sure these are added in the `operators` table of your MySQL database.

---

## 📦 Build Instructions

1. **Install dependencies**

```bash
pip install PySide6 mysql-connector-python
```

2. **Run the app**

```bash
python UI/login.py
```

3. **Package to .exe**

```bash
cd UI
pyinstaller --onefile --windowed login.py
```

- The `.exe` will be created in the `UI/dist/` folder

---

## 🎥 Demo Video

👉 [Link to Demo Video](#) *(upload to Drive or YouTube and paste the link here)*

---

## 📌 Notes

- Ensure MySQL is running and credentials are correct.
- Place any used product images in the `product_images/` folder.
- Use `main_dashboard.py` to navigate across forms after login.

---

## 📧 Contact

For any queries or clarifications, feel free to reach out.

---

**Developed By:** Deepthi Kousik

*Assignment project for internship / evaluation purposes.*

