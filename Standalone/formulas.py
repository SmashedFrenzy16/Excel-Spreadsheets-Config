from openpyxl import *

num1 = input("Enter in a number: ")

book = Workbook()

sheet = book.active

sheet["A1"] = num1