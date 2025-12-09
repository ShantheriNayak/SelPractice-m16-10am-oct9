##Create an Excel file with personal information (name, place, email) and save it to a specific location using Python.

## it will creaate a new workbook
from openpyxl import Workbook

## create a new excel workbook
workbook = Workbook()

##  to initialize the worksheet
worksheet = workbook.active
worksheet.title="Family_info"


##write data into the Personal_info excel sheet
worksheet['A1']='Sl_no'
worksheet['B1']='Name'
worksheet['C1']='Place'
worksheet['D1']='DOB'
worksheet['E1']='email-id'

data_list=[
    [1,'Shantheri','Bengaluru','22-10-1990','shanthi@gmail.com'],
    [2,'Prashanth','Bengaluru','19-04-1985','prash@gmail.com'],
    [3,'Pranav','Bengaluru','09-07-2018','pn1@gmail.com'],
    [4,'Praneeth','Bengaluru','16-11-2020','pn2@gmail.com'],

]

## adding /appending contents to excel file
for ele in data_list:
    worksheet.append(ele)

#save the excel file

workbook.save('Family_info.xlsx')


# ## to save the excel filein differnt location
workbook.save (r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files\Family_info.xlsx')
