# read file
from xlrd import open_workbook
# download file
from takehtml import get_url
import requests
# analyse file
from analyse_12science import analyse_12science, analyse_10
# write file
import xlsxwriter
import grequests

# import file name
excel_file = 'input/SSC Marks Entry 2019-20.xlsx'
try:
    readworkbook = open_workbook(excel_file, on_demand=True)
    workbook = xlsxwriter.Workbook('output/result1.xlsx')
except:
    print('%s file not found' % excel_file)
worksheet = workbook.add_worksheet()
# writeworkbook = copy(readworkbook)
i=0
url= []
indecies = {
    'seat': 'A',
    'name': 'B',
    'guj_board': 'C',
    'guj_school': 'D',
    'guj_total': 'E',
    'ss_board': 'F',
    'ss_school': 'G',
    'ss_total': 'H',
    'sci_board': 'I',
    'sci_school': 'J',
    'sci_total': 'K',
    'san_board': 'L',
    'san_school': 'M',
    'san_total': 'N',
    'eng_board': 'O',
    'eng_school': 'P',
    'eng_total': 'Q',
    'math_board': 'R',
    'math_school': 'S',
    'math_total': 'T',
    'total': 'U',
    'grade': 'V',
    'percentile': 'W'
}

for sheet in readworkbook.sheets():
    # writesheet = writebook.sheets()[0]
    for row in range(1, 3):
        roll = sheet.cell(row, 4).value
        roll = roll[0] + roll[2:]
        url.append(get_url(roll))
    
    rs = (grequests.get(u) for u in url)
    grequests.map(rs)
    # for key, value in ret.items():
    #     c_no = indecies.get(key, None)
    #     if c_no:
    #         worksheet.write(f'{c_no}{row+1}', value)

workbook.close()
readworkbook.release_resources()
# del readworkbook,sheet,i,writeworkbook,writesheet,analyse_value,roll