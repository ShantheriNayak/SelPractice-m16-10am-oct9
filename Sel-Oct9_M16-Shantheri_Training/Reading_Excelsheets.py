'''
xlrd: To read excel files, we use xlrd

to install xlrd
pip install xlrd 1.2.0

'''

import xlrd
##open the excel file
path=r'C'
workbook= xlrd.open_workbook(path)
print(workbook)         #book object

## open the worksheet
worksheet= workbook.sheet_by_name('candidates_data')
print(worksheet)            #sheet object

## converts the sheet object to generator object
rows= worksheeet.get_rows()
print(rows)
























































































































