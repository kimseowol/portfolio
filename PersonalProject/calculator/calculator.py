import sys
import os
import re
from PySide2 import QtWidgets, QtCore, QtUiTools


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # set UI
        ui_path = os.path.expanduser("/home/rapa/mycal.ui")
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.ui.show()

        # digit
        self.ui.number01.clicked.connect(self.btn_number01)
        self.ui.number02.clicked.connect(self.btn_number02)
        self.ui.number03.clicked.connect(self.btn_number03)
        self.ui.number04.clicked.connect(self.btn_number04)
        self.ui.number05.clicked.connect(self.btn_number05)
        self.ui.number06.clicked.connect(self.btn_number06)
        self.ui.number07.clicked.connect(self.btn_number07)
        self.ui.number08.clicked.connect(self.btn_number08)
        self.ui.number09.clicked.connect(self.btn_number09)
        self.ui.number0.clicked.connect(self.btn_number0)
        self.ui.number00.clicked.connect(self.btn_number00)
        # operator
        self.ui.button_del.clicked.connect(self.delete_number)
        self.ui.button_dot.clicked.connect(self.dot_number)
        self.ui.button_plus.clicked.connect(self.plus_number)
        self.ui.button_sub.clicked.connect(self.minus_number)
        self.ui.button_mult.clicked.connect(self.multiply_number)
        self.ui.button_divide.clicked.connect(self.divide_number)
        self.ui.button_result.clicked.connect(self.result_number)
        self.ui.button_reset.clicked.connect(self.reset_numbers)

    def btn_number01(self):
        self.number("1")

    def btn_number02(self):
        self.number("2")

    def btn_number03(self):
        self.number("3")

    def btn_number04(self):
        self.number("4")

    def btn_number05(self):
        self.number("5")

    def btn_number06(self):
        self.number("6")

    def btn_number07(self):
        self.number("7")

    def btn_number08(self):
        self.number("8")

    def btn_number09(self):
        self.number("9")

    # Below . could not be processed 0000 yet
    def btn_number0(self):
        exist_text = self.ui.lineEdit.text()
        check = re.compile('^0+')

        if check.fullmatch(exist_text):
            pass
        else:
            self.ui.lineEdit.setText(exist_text + "0")

    def btn_number00(self):
        exist_text = self.ui.lineEdit.text()
        if exist_text[-1].is_digit() or exist_text[-1] == ".":
            self.number("00")

    def number(self, num):
        exist_text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(exist_text + num)

    def is_digit(self):
        exist_text = self.ui.lineEdit.text()
        if (exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "/") | (exist_text[-1] == "*") | (exist_text[-1] == "."):
            self.delete_number()

    def delete_number(self):
        exist_text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(exist_text[:-1])

    def dot_number(self):
        exist_text = self.ui.lineEdit.text()
        if(exist_text[-1] == "+") or (exist_text[-1] == "-") or (exist_text[-1] == "/") | (exist_text[-1] == "*") or (exist_text[-1] == "."):
            pass
        if "." in exist_text.split("+")[-1]:
            pass
        else:
            self.ui.lineEdit.setText(exist_text+".")
        if "." in exist_text.split("-")[-1]:
            pass
        else:
            self.ui.lineEdit.setText(exist_text+".")
        if "." in exist_text.split("/")[-1]:
            pass
        else:
            self.ui.lineEdit.setText(exist_text+".")
        if "." in exist_text.split("*")[-1]:
            pass
        else:
            self.ui.lineEdit.setText(exist_text+".")

    def plus_number(self):
        self.is_digit()
        self.number("+")

    def minus_number(self):
        self.is_digit()
        self.number("-")

    def multiply_number(self):
        self.is_digit()
        self.number("*")

    def divide_number(self):
        self.is_digit()
        self.number("/")

    def result_number(self):
        exist_text = self.ui.lineEdit.text()
        if (exist_text[-1] == "+") or (exist_text[-1] == "-") or (exist_text[-1] == "/") or (exist_text[-1] == "*") or (exist_text[-1] == ".") or (exist_text[-1] == "="):
            self.delete_number()
        else:
            self.number("=")
            result = eval(exist_text)
            self.ui.lineEdit.setText(str(round(result, 6)))

    def reset_numbers(self):
        self.ui.lineEdit.setText("")


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication()
    myapp = MyApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()