from openpyxl import *
from openpyxl.chart import PieChart3D, Reference

while True:


    choice = input("Enter in your choice (1, 2, or 3): ")

    if choice == "1":

        name = input("Enter in the name of your Excel workbook (including extension): ")

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

        data2 = Reference(sheet, min_col=2, min_row=1, max_row=5)

        chart.add_data(data2, titles_from_data=True)

        chart.set_categories(labels)

        chart.title = "Most Popular Crisps Flavor"

        sheet.add_chart(chart, "A8")

        book.save(name)

    elif choice == "2":

        pass

    elif choice == "3": 

        pass

    else:

        print("Invalid choice!")
    
    input("Do you want to select another choice? (y/n): ")

    if choice == "n" or choice == "N":

        break