from PyQt5 import QtCore, QtGui, QtWidgets
from MainLogin import Ui_LoginWindow
from registrationNew import Ui_registrationPage
from AdminPanel import Ui_AdminPanel
from MainProfile import Ui_MainWindow

class Ui_MainUI(object):
    def __init__(self):
        self.is_logged_in = False  # Track login status
        self.is_admin = False  # Track if the user is an admin

    def setupUi(self, MainUI):
        MainUI.setObjectName("MainUI")
        MainUI.resize(800, 600)
        MainUI.setStyleSheet("background-color: rgb(111, 87, 130);")

        self.centralwidget = QtWidgets.QWidget(MainUI)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(200, 50, 400, 50))
        self.label_title.setStyleSheet("font: 20pt 'Verdana'; color: white;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        # Login Button
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(300, 150, 200, 40))
        self.pushButton_login.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_login.setObjectName("pushButton_login")

        # Registration Button
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setGeometry(QtCore.QRect(300, 210, 200, 40))
        self.pushButton_register.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_register.setObjectName("pushButton_register")

        # Admin Panel Button
        self.pushButton_admin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_admin.setGeometry(QtCore.QRect(300, 270, 200, 40))
        self.pushButton_admin.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_admin.setObjectName("pushButton_admin")

        # User Profile Button
        self.pushButton_profile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile.setGeometry(QtCore.QRect(300, 330, 200, 40))
        self.pushButton_profile.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_profile.setObjectName("pushButton_profile")

        # Quit Button
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(300, 390, 200, 40))
        self.pushButton_quit.setStyleSheet("background-color: rgb(252, 252, 252); font: 12pt 'Verdana'; color: rgb(12, 31, 45);")
        self.pushButton_quit.setObjectName("pushButton_quit")

        MainUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainUI)
        QtCore.QMetaObject.connectSlotsByName(MainUI)

        # Connect buttons to their respective functions
        self.pushButton_login.clicked.connect(self.open_login)
        self.pushButton_register.clicked.connect(self.open_registration)
        self.pushButton_admin.clicked.connect(self.open_admin_panel)
        self.pushButton_profile.clicked.connect(self.open_profile)
        self.pushButton_quit.clicked.connect(self.quit_application)

    def retranslateUi(self, MainUI):
        _translate = QtCore.QCoreApplication.translate
        MainUI.setWindowTitle(_translate("MainUI", "Main UI"))
        self.label_title.setText(_translate("MainUI", "Bank Fraud Detection System"))
        self.pushButton_login.setText(_translate("MainUI", "Login"))
        self.pushButton_register.setText(_translate("MainUI", "Register"))
        self.pushButton_admin.setText(_translate("MainUI", "Admin"))  # Renamed button
        self.pushButton_profile.setText(_translate("MainUI", "User Profile"))
        self.pushButton_quit.setText(_translate("MainUI", "Quit"))

    def open_login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.window, self.handle_login_result)
        self.window.show()

    def open_registration(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_admin_panel(self):
        if not self.is_logged_in or not self.is_admin:
            QtWidgets.QMessageBox.warning(None, "Access Denied", "You must log in as an admin to access the Admin Panel.")
            return
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminPanel()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_profile(self):
        if not self.is_logged_in:
            QtWidgets.QMessageBox.warning(None, "Access Denied", "You must log in to view the profile.")
            return
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def handle_login_result(self, success, is_admin=False):
        if success:
            self.is_logged_in = True
            self.is_admin = is_admin
        else:
            QtWidgets.QMessageBox.information(None, "Login Failed", "Account does not exist. Redirecting to registration.")
            self.open_registration()

    def quit_application(self):
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainUI = QtWidgets.QMainWindow()
    ui = Ui_MainUI()
    ui.setupUi(MainUI)
    MainUI.show()
    sys.exit(app.exec_())
