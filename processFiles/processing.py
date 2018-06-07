from openpyxl import load_workbook

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
