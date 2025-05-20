from PyQt5 import QtCore, QtWidgets

class Ui_FraudLogs(object):
    def setupUi(self, FraudLogs, fraud_logs):
        FraudLogs.setObjectName("FraudLogs")
        FraudLogs.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(FraudLogs)
        self.centralwidget.setObjectName("centralwidget")

        # Table to display fraud logs
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 700, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels([
            "FraudLog ID", "Transaction ID", "Reason", "Timestamp"
        ])

        # Populate table with fraud logs
        self.tableWidget.setRowCount(len(fraud_logs))
        for row_idx, row_data in enumerate(fraud_logs):
            for col_idx, col_data in enumerate(row_data[:4]):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        FraudLogs.setCentralWidget(self.centralwidget)

        self.retranslateUi(FraudLogs)
        QtCore.QMetaObject.connectSlotsByName(FraudLogs)

    def retranslateUi(self, FraudLogs):
        _translate = QtCore.QCoreApplication.translate
        FraudLogs.setWindowTitle(_translate("FraudLogs", "Fraud Logs"))