from openpyxl import *

name = input("Ennter in the name of your Excel workbook: ")

sheet_name1 = input("Enter in the name of the first sheet: ")

sheet_name2 = input("Enter in the name of the second sheet: ")

def sheet_creator(file):
  
  book = Workbook()
  
  sheet = book.active
  
  sheet.title = sheet_name1

  sheet2 = book.create_sheet(title=sheet_name2)
