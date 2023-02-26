from openpyxl import *

num1 = input("Enter in a number: ")

num2 = input("Enter in another number: ")

book = Workbook()

sheet = book.active

sheet["A1"] = num1

sheet["B1"] = num2