from openpyxl import load_workbook #либу я поставил
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()
results = cursor.fetchall()

wb = load_workbook('./22.xlsx') #файлик сюда закинь тоже сам, чтобы все в проекте было и назови по другому

sheet_name = u'sheet'
sheet = wb.get_sheet_by_name(sheet_name)


n = 10
j = 2 # тебе сначала надо заполнить таблицу с СЗИ потом заполнять связующую...
while j < n:
    b = str(j)
    print(sheet['A' + b + ''].value)
    print(sheet['B' + b + ''].value)
    print(sheet['C' + b + ''].value)
    print(sheet['D' + b + ''].value)
    print(sheet['E' + b + ''].value)
    print(sheet['F' + b + ''].value)
    result = cursor.execute('INSERT INTO landing_defence VALUES (?, ?, ?, ?, ?, ?)', (int(sheet['A' + b + ''].value), str(sheet['B' + b + ''].value), str(sheet['C' + b + ''].value), sheet['D' + b + ''].value, str(sheet['E' + b + ''].value), str(sheet['F' + b + ''].value)))
    conn.commit()
    j = j + 1

print("success")