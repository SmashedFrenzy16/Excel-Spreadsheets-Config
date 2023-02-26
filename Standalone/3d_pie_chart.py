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

labels = Reference(sheet, min_col=1, min_row=2, max_row=5)

data2 = Reference(ws, min_col=2, min_row=1, max_row=5)

chart.add_data(data2, titles_from_data=True)
