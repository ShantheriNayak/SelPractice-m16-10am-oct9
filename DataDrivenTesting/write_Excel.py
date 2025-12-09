'''
openpyxl

installation-->comd prompt-->pip install openpyxl

'''

from openpyxl import Workbook # it will creaate a new workbook
workbook = Workbook()  ## create a new excel workbook

## we have to initialize the worksheet
worksheet = workbook.active

## set the title for the worksheet(optional)
worksheet.title='M16_data'

## write the data into the excell file
worksheet['A1']='name'
worksheet['B1']='place'
worksheet['C1']='Phone_num'
worksheet['D1']='email-id'

data_list=[
    ['Shantheri','Bengaluru',9087567654,'shanthi@gamil.com'],
    ['Chaitra maam','Bengaluru',9087568954,'chaitra@gamil.com'],
    ['Shyam Sundar Sir','Bengaluru',9082357654,'sundar@gamil.com'],
    ['Ramya Maam', 'Bengaluru', 9085567654, 'ramya@gamil.com']
]

for ele in data_list:
    worksheet.append(ele)

## save the excel file
#workbook.save('M16_data.xlsx')

# ## to save the excel filein differnt location
workbook.save (r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files\M16_data.xlsx')













































































































