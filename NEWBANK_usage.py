from PyQt5 import QtCore, QtWidgets
import sqlite3

class Ui_UserManagement(object):
    def setupUi(self, UserManagement):
        UserManagement.setObjectName("UserManagement")
        UserManagement.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(UserManagement)
        self.centralwidget.setObjectName("centralwidget")

        # Table to display users
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)  # Adjust based on your database schema
        self.tableWidget.setHorizontalHeaderLabels(["User ID", "Username", "Role"])

        # Add User Button
        self.pushButton_add_user = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_user.setGeometry(QtCore.QRect(50, 470, 150, 40))
        self.pushButton_add_user.setText("Add User")
        self.pushButton_add_user.setObjectName("pushButton_add_user")

        # Delete User Button
        self.pushButton_delete_user = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_user.setGeometry(QtCore.QRect(220, 470, 150, 40))
        self.pushButton_delete_user.setText("Delete User")
        self.pushButton_delete_user.setObjectName("pushButton_delete_user")

        UserManagement.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserManagement)
        QtCore.QMetaObject.connectSlotsByName(UserManagement)

        # Load users into the table
        self.load_users()

        # Connect buttons to their respective functions
        self.pushButton_add_user.clicked.connect(self.add_user)
        self.pushButton_delete_user.clicked.connect(self.delete_user)

    def retranslateUi(self, UserManagement):
        _translate = QtCore.QCoreApplication.translate
        UserManagement.setWindowTitle(_translate("UserManagement", "User Management"))

    def load_users(self):
        """Load users from the database into the table."""
        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()
        cur.execute("SELECT id, username, role FROM Users")
        users = cur.fetchall()
        conn.close()

        self.tableWidget.setRowCount(len(users))
        for row_idx, row_data in enumerate(users):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    def add_user(self):
        """Add a new user to the database."""
        username, ok = QtWidgets.QInputDialog.getText(None, "Add User", "Enter username:")
        if ok and username:
            role, ok = QtWidgets.QInputDialog.getText(None, "Add User", "Enter role (e.g., admin, user):")
            if ok and role:
                conn = sqlite3.connect("BankNH.db")
                cur = conn.cursor()
                try:
                    cur.execute("INSERT INTO Users (username, role) VALUES (?, ?)", (username, role))
                    conn.commit()
                    QtWidgets.QMessageBox.information(None, "Success", "User added successfully!")
                    self.load_users()
                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.critical(None, "Error", f"Failed to add user: {e}")
                finally:
                    conn.close()

    def delete_user(self):
        """Delete the selected user from the database."""
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a user to delete.")
            return

        user_id = self.tableWidget.item(selected_row, 0).text()
        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM Users WHERE id = ?", (user_id,))
            conn.commit()
            QtWidgets.QMessageBox.information(None, "Success", "User deleted successfully!")
            self.load_users()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to delete user: {e}")
        finally:
            conn.close()

# When updating or querying balances, always use:
# cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (username,))
# cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?", (new_balance, username))