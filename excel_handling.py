from xlrd import open_workbook
from analyse_12science import analyse_12science
from xlutils.copy import copy
from takehtml import make_html

excel_file = 'one_class.xlsx'
try:
    readworkbook = open_workbook(excel_file, on_demand=True)
except:
    print('%s file not found' % excel_file)

writeworkbook = copy(readworkbook)
i=0
for sheet in readworkbook.sheets():
    writesheet = writeworkbook.get_sheet(i)
    for row in range(sheet.nrows)[1:]:
        rolln = sheet.cell(row, 0).value
        roll = 'B' + str(rolln)
        roll = str(roll)[:7]
        make_html(roll)
        analyse_value = analyse_12science(roll)
        for col in range(len(analyse_value)):
            writesheet.write(row, col + 1, analyse_value[col])
        i=i+1

writeworkbook.save(excel_file)
readworkbook.release_resources()
del readworkbook,sheet,i,writeworkbook,writesheet,analyse_value,roll