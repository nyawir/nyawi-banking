from PyQt5 import QtCore, QtWidgets

class Ui_TransactionLogs(object):
    def setupUi(self, TransactionLogs, transactions):
        TransactionLogs.setObjectName("TransactionLogs")
        TransactionLogs.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(TransactionLogs)
        self.centralwidget.setObjectName("centralwidget")

        # Table to display transaction logs
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels([
            "Transaction ID", "Sender", "Receiver", "Type", "Amount",
            "Sender Old Balance", "Sender New Balance",
            "Receiver Old Balance", "Receiver New Balance"
        ])

        # Populate table with transaction logs
        self.tableWidget.setRowCount(len(transactions))
        for row_idx, row_data in enumerate(transactions):
            for col_idx, col_data in enumerate(row_data[:9]):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        TransactionLogs.setCentralWidget(self.centralwidget)

        self.retranslateUi(TransactionLogs)
        QtCore.QMetaObject.connectSlotsByName(TransactionLogs)

    def retranslateUi(self, TransactionLogs):
        _translate = QtCore.QCoreApplication.translate
        TransactionLogs.setWindowTitle(_translate("TransactionLogs", "Transaction Logs"))
