from openpyxl import *

name = input("Enter in the name of your Excel workbook (including extension): ")

num1 = input("Enter in a number: ")

num2 = input("Enter in another number: ")

book = Workbook()

sheet = book.active

sheet["A1"] = num1

sheet["B1"] = num2

sheet["C1"] = "SUM(A1, B1)"

sheet["D1"] = "IF(A1>B1, \"A1 is greater than B1\", \"B1 is greater than A1\")"

book.save(name)