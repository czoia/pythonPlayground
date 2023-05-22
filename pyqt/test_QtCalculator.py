from unittest import TestCase
from calculator_mainwindow import Calculator_MainWindow
from QtCalculator import MainWindow


class TestMainWindow(TestCase):
    def test__build_expression_regex(self):
        import re
        test_cases = {
            "123+345": ["123", "+", "345"],
            "123-345": ["123", "-", "345"],
            "123*345": ["123", "*", "345"],
            "123/345": ["123", "/", "345"],
            "123-345%": ["123", "-", "345", "%"],
            Calculator_MainWindow.SQUARE_RADIX_CHAR + "123": [Calculator_MainWindow.SQUARE_RADIX_CHAR, "123"],
            "123^345": ["123", "^", "345"],
            "(123)": ['(', "123", ')'],
            "123*(345)": ["123", "*", '(', "345", ')'],
            "123+345-678": ["123", "+", "345", "-", "678"],

        }

        for exp, expected in test_cases.items():
            splitted = [a for a in filter(None, re.split("(\+|-|\*|\(|\)|\^|/|%|" + Calculator_MainWindow.SQUARE_RADIX_CHAR+")", exp))]
            self.assertListEqual(splitted, expected, f"original expression: {exp}")

    def test__build_expression(self):
        window = MainWindow(True)

        test_cases = {
            "1": "1",
            "123+345": "468",
            "123-345": "-222",
            "123*345": "42435",
            "123/345": "0.3565217391304348",
            # "123-345%": "−301.35",
            Calculator_MainWindow.SQUARE_RADIX_CHAR + "123": "11.090536506409418",
            Calculator_MainWindow.SQUARE_RADIX_CHAR + "(123*345)": "205.99757280123472",
            Calculator_MainWindow.SQUARE_RADIX_CHAR + "123*345": "3826.235094711249",
            "123*" + Calculator_MainWindow.SQUARE_RADIX_CHAR + "345": "2284.623601383825",
            "3^4": "81",
            "(123)": "123",
            "123": "123",
            "123*(345)": "42435",
            "123*(345-12)": "40959",
            "123+345-678": "-210",
            "123*(345-12": window.ERROR_MSG,
            "123*((345-12)": window.ERROR_MSG,
            "123*(345-12)))": window.ERROR_MSG,
            "123-": "123",
            "123*345-": "42435",
            "123*(345-": window.ERROR_MSG,
            "123*345-)": window.ERROR_MSG,
        }

        for exp, expected in test_cases.items():
            self.assertEqual(expected, window._build_expression(exp), f"original expression: {exp}")
