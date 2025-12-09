import xlrd

def reading_testdata(path, sheetname):
    workbook = xlrd.open_workbook(path)   ## book obj
    worksheet = workbook.sheet_by_name(sheetname) ## Sheet obj
    rows=worksheet.get_rows()
    header=next(rows)               ## removes the header names "var_name" and "value"

    d={}
    for ele in rows:
        d[ele[0].value]=ele[4].value   ## shows only key value pair

    return d



### d[ele[0].value]=ele[1].value # to read first column data1 from excel file
###d[ele[0].value]=ele[2].value # to read first column data2 from excel file
###d[ele[0].value]=ele[3].value # to read first column data3 from excel file