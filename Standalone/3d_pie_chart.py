from openpyxl import *

from openpyxl.chart import PieChart3D, Reference

data = [

    ["Crisps", "Sold"],
    ["Salty", 100],
    ["Onion", 94],
    ["Chilli", 88],
    ["Chicken", 54],
    ["Bacon", 21],
]

book = Workbook()

sheet = book.active

for row in data:

    sheet.append(row)

chart = PieChart3D()