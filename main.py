import os
import openpyxl


workbook = os.path.join('FailureData', 'FailureList for 4 mounths 2019 (SVRD).xlsx')

sheetName = 'Лист1'

sheet = openpyxl.load_workbook(workbook)[sheetName]

for line in sheet['A1:I2']:
    print(line)

print(line[0].value)
