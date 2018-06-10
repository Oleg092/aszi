from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("select * from landing_users")
results = cursor.fetchall()

wb = load_workbook('./1.xlsx')

sheet = wb.get_sheet_by_name('sheet')
n = 111
i = 1
while i < n:
    c = str(i)  # Ну и конечно же, вместо вывода в консоль тут можно сделать запись данных в базу ;)
    print(sheet['A' + c + ''].value)
    print(sheet['B' + c + ''].value)
    print(sheet['C' + c + ''].value)
    print(sheet['D' + c + ''].value)
    print(sheet['E' + c + ''].value)
    i = i + 1

print(results)