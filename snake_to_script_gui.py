from PyQt5 import QtCore, QtWidgets
from python_to_js_converter import python_to_javascript


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
        self.convert_button.setEnabled(False)

        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(930, 570, 131, 28))
        self.copy_button.setObjectName("copy_button")
        self.copy_button.setEnabled(False)

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
        self.plainTextEdit.textChanged.connect(self.updateConvertButtonState)
        self.textBrowser.textChanged.connect(self.updateCopyButtonState)

    def convertCode(self):
        try:
            python_code = self.plainTextEdit.toPlainText()
            javascript_code = python_to_javascript(python_code)

            # Remove the runtime import and __name__ assignment
            javascript_lines = javascript_code.split('\n')
            cleaned_js_code = '\n'.join(line for line in javascript_lines
                                        if not line.startswith('import')
                                        and not line.startswith('var __name__'))

            self.textBrowser.setText(cleaned_js_code)

            if cleaned_js_code.startswith("// Error"):
                self.statusbar.showMessage("Conversion failed. See output for details.", 5000)
            elif cleaned_js_code.strip() == "":
                self.statusbar.showMessage("Conversion produced no output. Check your Python code.", 5000)
            else:
                self.statusbar.showMessage("Conversion successful", 3000)
        except Exception as e:
            self.statusbar.showMessage(f"An error occurred: {str(e)}", 5000)
            print(f"Error in convertCode: {str(e)}", file=sys.stderr)

    def copyCode(self):
        javascript_code = self.textBrowser.toPlainText()
        QtWidgets.QApplication.clipboard().setText(javascript_code)
        self.statusbar.showMessage("Code copied to clipboard", 3000)

    def updateConvertButtonState(self):
        self.convert_button.setEnabled(bool(self.plainTextEdit.toPlainText().strip()))

    def updateCopyButtonState(self):
        self.copy_button.setEnabled(bool(self.textBrowser.toPlainText().strip()))