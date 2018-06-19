from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()
results = cursor.fetchall()

wb = load_workbook('./22.xlsx')

sheet_name = u'sheet'
sheet = wb.get_sheet_by_name(sheet_name)

n = 52
j = 2
while j < n:
    b = str(j)
    d = str(sheet['D' + b + ''].value)
    d = d[0:10]
    print(sheet['A' + b + ''].value)
    print(sheet['B' + b + ''].value)
    print(sheet['C' + b + ''].value)
    print(d)
    print(sheet['E' + b + ''].value)
    print(sheet['F' + b + ''].value)
    result = cursor.execute('INSERT INTO landing_defence VALUES (?, ?, ?, ?, ?, ?)', (int(sheet['A' + b + ''].value), str(sheet['B' + b + ''].value), str(sheet['C' + b + ''].value), d, str(sheet['E' + b + ''].value), str(sheet['F' + b + ''].value)))
    conn.commit()
    j = j + 1

print("success")