from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()
results = cursor.fetchall()

wb = load_workbook('1.xlsx')

sheet = wb.get_sheet_by_name('sheet')
n = 111
i = 2
while i < n:
    c = str(i)  # Ну и конечно же, вместо вывода в консоль тут можно сделать запись данных в базу ;)
    print(sheet['A' + c + ''].value)
    print(sheet['B' + c + ''].value)
    print(sheet['C' + c + ''].value)
    print(sheet['D' + c + ''].value)
    print(sheet['E' + c + ''].value)
    result = cursor.execute('insert into landing_requirements values (?, ?, ?, ?, ?, ?)', (sheet['A' + c + ''].value, sheet['B' + c + ''].value, sheet['C' + c + ''].value, sheet['D' + c + ''].value, int(sheet['F' + c + ''].value), str(sheet['F' + c + ''].value)))
    conn.commit()
    i = i + 1

print("success")
