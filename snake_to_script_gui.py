# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class SnakeToScriptGui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 660)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 60, 1020, 200))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 330, 121, 16))
        self.label_2.setObjectName("label_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 350, 1020, 200))
        self.textBrowser.setObjectName("textBrowser")

        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(930, 280, 131, 28))
        self.convert_button.setObjectName("convert_button")

        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(930, 570, 131, 28))
        self.copy_button.setObjectName("copy_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connectSignalsSlots()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SnakeToScript"))
        self.label.setText(_translate("MainWindow", "Python code:"))
        self.label_2.setText(_translate("MainWindow", "JavaScript code:"))
        self.convert_button.setText(_translate("MainWindow", "Convert the code"))
        self.copy_button.setText(_translate("MainWindow", "Copy the code"))

    def connectSignalsSlots(self):
        self.convert_button.clicked.connect(self.convertCode)
        self.copy_button.clicked.connect(self.copyCode)

    def convertCode(self):
        # TODO: Implement code conversion logic
        python_code = self.plainTextEdit.toPlainText()
        # Convert Python to JavaScript (implement this functionality)
        javascript_code = f"// Converted from Python:\n{python_code}"
        self.textBrowser.setText(javascript_code)

    def copyCode(self):
        javascript_code = self.textBrowser.toPlainText()
        QtWidgets.QApplication.clipboard().setText(javascript_code)
        self.statusbar.showMessage("Code copied to clipboard", 3000)