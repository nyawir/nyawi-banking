from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(800, 600)
        AdminPanel.setStyleSheet("background-color: rgb(111, 87, 130);")

        self.centralwidget = QtWidgets.QWidget(AdminPanel)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(200, 20, 400, 50))
        self.label_title.setStyleSheet("font: 20pt 'Verdana'; color: white;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        # Manage Users Button
        self.pushButton_manage_users = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_manage_users.setGeometry(QtCore.QRect(300, 100, 200, 40))
        self.pushButton_manage_users.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_manage_users.setObjectName("pushButton_manage_users")

        # View Transactions Button
        self.pushButton_view_transactions = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view_transactions.setGeometry(QtCore.QRect(300, 160, 200, 40))
        self.pushButton_view_transactions.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_view_transactions.setObjectName("pushButton_view_transactions")

        # View Fraud Logs Button
        self.pushButton_view_fraud_logs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view_fraud_logs.setGeometry(QtCore.QRect(300, 220, 200, 40))
        self.pushButton_view_fraud_logs.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_view_fraud_logs.setObjectName("pushButton_view_fraud_logs")

        # Logout Button
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(300, 280, 200, 40))
        self.pushButton_logout.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_logout.setObjectName("pushButton_logout")

        AdminPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPanel)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

        # Connect buttons to their respective functions
        self.pushButton_manage_users.clicked.connect(self.manage_users)
        self.pushButton_view_transactions.clicked.connect(self.view_transactions)
        self.pushButton_view_fraud_logs.clicked.connect(self.view_fraud_logs)
        self.pushButton_logout.clicked.connect(self.logout)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "Admin"))
        self.label_title.setText(_translate("AdminPanel", "Admin Panel"))
        self.pushButton_manage_users.setText(_translate("AdminPanel", "Manage Users"))
        self.pushButton_view_transactions.setText(_translate("AdminPanel", "View Transactions"))
        self.pushButton_view_fraud_logs.setText(_translate("AdminPanel", "View Fraud Logs"))
        self.pushButton_logout.setText(_translate("AdminPanel", "Logout"))

    def manage_users(self):
        print("Manage Users clicked")
        # Add functionality to view, add, delete, or update users in the database

    def view_transactions(self):
        print("View Transactions clicked")
        # Add functionality to display transaction logs from the database

    def view_fraud_logs(self):
        print("View Fraud Logs clicked")
        # Add functionality to display flagged transactions

    def logout(self):
        print("Logout clicked")
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminPanel = QtWidgets.QMainWindow()
    ui = Ui_AdminPanel()
    ui.setupUi(AdminPanel)
    AdminPanel.show()
    sys.exit(app.exec_())