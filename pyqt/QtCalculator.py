import math
import sys
import re
from functools import partial

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, SIGNAL

from calculator_mainwindow import Calculator_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    ERROR_MSG = "Something wrong with the expression"

    def __init__(self, test: bool = False):
        if not test:
            super(MainWindow, self).__init__()

            self.special_buttons = ["A/C", Calculator_MainWindow.PLUS_MINUS_CHAR, "%", Calculator_MainWindow.ROLLBACK_CHAR,
                                    "="]

            self.ui = Calculator_MainWindow()
            self.ui.setupUi(self)
            self._connect_signal_and_slot()
        self.operation_symbol = ["+", "-", "*", "/", "^", "%", Calculator_MainWindow.SQUARE_RADIX_CHAR]
        self.operation_stack = list()

    def _connect_signal_and_slot(self):
        for key in self.ui.map_buttons:
            if key not in self.special_buttons:
                self.ui.map_buttons[key].connect(SIGNAL('clicked()'),
                                                 partial(self._insert_value, self.ui.map_buttons[key].text()))

        for key in self.special_buttons:
            self.ui.map_buttons[key].connect(SIGNAL('clicked()'),
                                             partial(self._handle_special_case, self.ui.map_buttons[key].text()))

    def _insert_value(self, value):
        self.ui.inputLine.setText(self.ui.inputLine.text() + value)

    def _handle_special_case(self, value):
        if value == 'A/C':
            self.ui.inputLine.clear()
            self.operation_stack.clear()
        elif value == Calculator_MainWindow.PLUS_MINUS_CHAR:
            text = self.ui.inputLine.text()
            idx = max(text.rfind(i) for i in ")(+-/*")
            if idx <= 0:
                # sign not found or at the beginning
                if text[0] == '-':
                    text = text[1:]
                else:
                    text = '-' + text
            else:
                if text[idx] == '-':
                    text = text[:idx] + text[idx + 1:]
                else:
                    text = text[:idx + 1] + '-' + text[idx + 1:]
            self.ui.inputLine.setText(text)
        elif value == Calculator_MainWindow.ROLLBACK_CHAR:
            self.ui.inputLine.setText(self.ui.inputLine.text()[:-1])
        elif value == '+':
            self._build_expression(self.ui.inputLine.text())

    def _build_expression(self, text_expression: str) -> str:
        expr = [a for a in filter(None,
                                  re.split(r"(\+|-|\*|\(|\)|\^|/|%|" + Calculator_MainWindow.SQUARE_RADIX_CHAR+")",
                                           "(" + text_expression + ")"))]

        def base_case(val1: float, _op: str, _val2: float = None) -> float:
            if _op == "+":
                return val1 + (_val2 if _val2 is not None else 0)
            elif _op == "-":
                return val1 - (_val2 if _val2 is not None else 0)
            elif _op == "*":
                return val1 * (_val2 if _val2 is not None else 1)
            elif _op == "/":
                return val1 / (_val2 if _val2 is not None else 1)
            elif _op == "^":
                return math.pow(val1, _val2)
            elif _op == '%':
                return val1 / 100
            else:
                raise ValueError(f"Unrecognized operation: [{_op}]")

        expr.reverse()
        res = 0
        count_parenthesis = 0
        for elem in expr:
            if elem == "(":
                count_parenthesis -= 1
                partial = self.operation_stack.pop()
                i = 0
                while i < len(self.operation_stack):
                    op = self.operation_stack.pop()
                    try:
                        val2 = self.operation_stack.pop()
                    except IndexError:
                        val2 = None
                    partial = base_case(partial, op, val2)
                self.operation_stack.append(partial)
            elif elem == ")":
                count_parenthesis += 1
            elif elem == Calculator_MainWindow.SQUARE_RADIX_CHAR:
                try:
                    self.operation_stack.append(math.sqrt(self.operation_stack.pop()))
                except IndexError:
                    return self.ERROR_MSG
            else:
                # try to convert to number
                try:
                    self.operation_stack.append(elem if elem in self.operation_symbol else float(elem))
                except ValueError:
                    return self.ERROR_MSG

        if len(self.operation_stack) != 1:
            res = self.ERROR_MSG
        else:  # use-case: user insert only a number and press =
            res = self.operation_stack.pop()
        return str(int(res) if res.is_integer() else res) if count_parenthesis == 0 else self.ERROR_MSG


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
