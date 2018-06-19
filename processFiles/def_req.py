from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()
results = cursor.fetchall()

wb = load_workbook('./21.xlsx')

sheet_name = u'Defence'
sheet = wb.get_sheet_by_name(sheet_name)
d = dict([(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E"), (6, "F"), (7, "G"), (8, "H"), (9, "I"), (10, "J"), (11, "K"), (12, "L"), (13, "M"), (14, "N"), (15, "O"), (16, "P"), (17, "Q"), (18, "R"), (19, "S"), (20, "T"),(21, "U"), (22, "V"), (23, "W"), (24, "X"), (25, "Y"), (26, "Z"), (27, "AA"), (28, "AB"), (29, "AC"), (30, "AD"),(31, "AE"), (32, "AF"), (33, "AG"), (34, "AH"), (35, "AI"), (36, "AJ"), (37, "AK"), (38, "AL"), (39, "AM"), (40, "AN"),(41, "AO"), (42, "AP"), (43, "AQ"), (44, "AR"), (45, "AS"), (46, "AT"), (47, "AU"), (48, "AV"), (49, "AW"), (50, "AX"),(51, "AY")])#создание словаря для перемещения по буквенным значениям exel файла
n = 52
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
