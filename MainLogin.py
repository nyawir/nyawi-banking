import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from MainProfile import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

#
# from faker import Faker
#
# # Specify the database filename
db_filename = 'BankMT.db'

# Create a connection to the database (this will also create the database file)
conn = sqlite3.connect(db_filename)

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS MTBANK (

    TYPE TEXT,
    AMOUNT INTEGER,
    SENDER TEXT,
    SENDEROLDBAL INTEGER,
    SENDERNEWBAL INTEGER,
    RECEIVER TEXT,
    RECOLDBAL INTEGER,
    RECNEWBAL INTEGER
);
'''
cursor.execute(create_table_query)

# Create the NEWBANK table with an IS_ADMIN column
create_table_query = '''
CREATE TABLE IF NOT EXISTS NEWBANK (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL,
    IS_ADMIN INTEGER DEFAULT 0  -- 0 for regular users, 1 for admin users
);
'''
cursor.execute(create_table_query)

# Check if admin credentials already exist
cursor.execute("SELECT * FROM NEWBANK WHERE USERNAME = 'admin' AND IS_ADMIN = 1")
if not cursor.fetchone():  # If no record is found
    # Insert admin credentials
    cursor.execute("INSERT INTO NEWBANK (USERNAME, PASSWORD, IS_ADMIN) VALUES ('admin', 'admin123', 1)")
    conn.commit()
    print("Admin credentials added to the database.")
else:
    print("Admin credentials already exist.")

c = conn.cursor()
conn.commit()
class Ui_LoginWindow(object):
    def beginLogin(self, LoginWindow, callback):
        self.login = LoginWindow
        self.callback = callback  # Callback to handle login result
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(553, 166)
        LoginWindow.setStyleSheet("background-color: rgb(111, 87, 130);\n"
"")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgba(240, 240, 240, 240);")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgba(240, 240, 240, 240);")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Login.setStyleSheet("color: rgb(240, 240, 240);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(78, 78, 78);")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_Login)
        self.pushButton_Sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sign_up.setStyleSheet("color: rgb(240, 240, 240);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(78, 78, 78);")
        self.pushButton_Sign_up.setObjectName("pushButton_Sign_up")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton_Sign_up)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/login_avater_9RD_icon.ico"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        ####################################################
        #         Connecting welcome page button 
        ####################################################

        self.pushButton_Login.clicked.connect(self.loginLogin)
        self.pushButton_Sign_up.clicked.connect(self.reg)

    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()


    def profile(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def open_admin_panel(self):
        from AdminPanel import Ui_AdminPanel
        self.AdminPanel = QtWidgets.QMainWindow()
        self.ui = Ui_AdminPanel()
        self.ui.setupUi(self.AdminPanel)
        self.AdminPanel.show()

    def loginLogin(self):
        import sqlite3
        dbb = sqlite3.connect('BankNH.db')
        cur = dbb.cursor()
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()

        # Check for admin credentials
        if username == "admin" and password == "admin123":
            self.callback(True, is_admin=True)
            self.open_admin_panel()
        else:
            # Check for regular user credentials
            cur.execute("SELECT * FROM NEWBANK WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
            result = cur.fetchone()

            if result:
                is_admin = result[2] == 1  # Check if the user is an admin
                self.callback(True, is_admin=is_admin)
                self.profile()  # Open the user profile if credentials are valid
            else:
                QtWidgets.QMessageBox.warning(None, "Login Error", "Invalid username or password. Redirecting to sign-up.")
                self.callback(False)
                self.login.close()

    def reg(self):
        self.login.close()
        from registrationNew import Ui_registrationPage
        self.general_message('Back', 'Will you like to go Back')
        self.registrationPage = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.show()
        
        

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Page"))
        self.label_2.setText(_translate("LoginWindow", "UserName"))
        self.label_3.setText(_translate("LoginWindow", "PassWord"))
        self.pushButton_Login.setText(_translate("LoginWindow", "LOGIN"))
        self.pushButton_Sign_up.setText(_translate("LoginWindow", "BACK TO SIGN-UP PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.beginLogin(LoginWindow, lambda success, is_admin: print("Login success:", success, "Is Admin:", is_admin))
    LoginWindow.show()
    sys.exit(app.exec_())

