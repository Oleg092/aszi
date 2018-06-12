from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()
results = cursor.fetchall()

wb = load_workbook('./21.xlsx')

sheet_name = u'Defence'
sheet = wb.get_sheet_by_name(sheet_name)
d = dict([(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E"), (6, "F"), (7, "G"), (8, "H"), (9, "I")])#создание словаря для перемещения по буквенным значениям exel файла
n = 10
j = 1 # номер СЗИ
c = 110
id = 2
while j < n:
    i = 1  # Номер Требования
    while i < c:
        print(d[j])
        print(i)
        print(sheet[''+d[j]+'' + str(i) + ''].value)
        if sheet[''+d[j]+'' + str(i) + ''].value == 1:
            print("true")
            result = cursor.execute('INSERT INTO landing_defence_requirements VALUES (?, ?, ?)', (id, j, i))
            conn.commit()
            id = id + 1
        i = i + 1
    j = j + 1

print("success")