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
        
        # connect digits 
        self.ui.number01.clicked.connect(lambda: self.btn_number('1'))
        self.ui.number02.clicked.connect(lambda: self.btn_number('2'))
        self.ui.number03.clicked.connect(lambda: self.btn_number('3'))
        self.ui.number04.clicked.connect(lambda: self.btn_number('4'))
        self.ui.number05.clicked.connect(lambda: self.btn_number('5'))
        self.ui.number06.clicked.connect(lambda: self.btn_number('6'))
        self.ui.number07.clicked.connect(lambda: self.btn_number('7'))
        self.ui.number08.clicked.connect(lambda: self.btn_number('8'))
        self.ui.number09.clicked.connect(lambda: self.btn_number('9'))

        # connect operations
        self.ui.button_plus.clicked.connect(lambda: self.btn_operations('+'))
        self.ui.button_sub.clicked.connect(lambda: self.btn_operations('-'))
        self.ui.button_mult.clicked.connect(lambda: self.btn_operations('*'))
        self.ui.button_divide.clicked.connect(lambda: self.btn_operations('/'))

        # connect buttons
        self.ui.number0.clicked.connect(self.btn_number0)
        self.ui.number00.clicked.connect(self.btn_number00)
        self.ui.button_del.clicked.connect(self.delete_number)
        self.ui.button_dot.clicked.connect(self.dot_number)
        self.ui.button_result.clicked.connect(self.result_number)
        self.ui.button_reset.clicked.connect(self.reset_numbers)

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

    def btn_operations(self, operations):
        exist_text = self.ui.lineEdit.text()
        if (exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "/") | (exist_text[-1] == "*") | (
                exist_text[-1] == "."):
            self.delete_num()
        self.btn_number(operations)

    def btn_number(self, num):
        exist_text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(exist_text + num)

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
