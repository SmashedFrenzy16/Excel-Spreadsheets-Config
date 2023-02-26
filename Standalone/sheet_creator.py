from openpyxl import *


sheet_name1 = input("Enter in the name of the first sheet: ")

sheet_name2 = input("Enter in the name of the second sheet: ")

def sheet_creator():
  
  book = Workbook()
  
  sheet = book.active
  
  sheet.title = sheet_name1
