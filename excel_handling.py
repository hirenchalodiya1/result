# read file
from xlrd import open_workbook
# download file
from takehtml import make_html, get_url
import requests
# analyse file
from analyse_12science import analyse_12science, analyse_10, analyse_12com
# write file
import xlsxwriter

# import file name
excel_file = 'input/HSC 2019-20.xlsx'
try:
    readworkbook = open_workbook(excel_file, on_demand=True)
    workbook = xlsxwriter.Workbook('output/result-hsc.xlsx')
except:
    print('%s file not found' % excel_file)
worksheet = workbook.add_worksheet()
# writeworkbook = copy(readworkbook)
indecies_10 = {
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
indecies = {
    'seat': 'A',
    'name': 'B',
    'percentile': 'C',
    'grade': 'D',
    'guj': 'E', 
    'eng':   'F',
    'echo': 'G', 
    'orc': 'H', 
    'stats': 'I', 
    'account': 'J', 
    'sec_prac': 'K'
}
for sheet in readworkbook.sheets():
    # writesheet = writebook.sheets()[0]
    for row in range(0, sheet.nrows):
        roll = sheet.cell(row, 2).value
        try:
            # make_html(roll)
            # preparing url
            url = f'http://gseb.org/3015ecruosnepo/gen/{roll[:3]}/{roll[3:5]}/{roll}.html'
            res = requests.get(url)
            content = res.text
            # with open(f'temp/{roll}.html', 'r') as f:
            #     content = f.read()
            ret = analyse_12com(content)
            print(f'{roll} looked up...')
            for key, value in ret.items():
                c_no = indecies.get(key, None)
                if c_no:
                    worksheet.write(f'{c_no}{row+1}', value)
        except KeyboardInterrupt:
            exit(0)
        except Exception as err:
            raise err
            
        
workbook.close()
readworkbook.release_resources()
# del readworkbook,sheet,i,writeworkbook,writesheet,analyse_value,roll