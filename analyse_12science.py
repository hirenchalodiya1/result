from bs4 import BeautifulSoup 
import re

def analyse_12science(content):
    soup = BeautifulSoup(content, 'html.parser')
    subject = []
    marks = []
    grade = []
    temp = []
    for tr in soup.find_all('tr'):
        spans = tr.find_all('span')
        if (len(spans) == 0):
            pass
        elif (len(spans) == 1):
            temp.append(spans[0].get_text())
        elif (len(spans) == 2):
            temp.append(spans[0].get_text())
            temp.append(spans[1].get_text())
        else:
            subject.append(spans[0].get_text())
            marks.append(spans[2].get_text())
            grade.append(spans[3].get_text())

    ret = {}
    for value in temp:
        if 'Seat No' in value:
            ret['seat'] = re.sub('Seat No: ', '', value)
        elif 'Name' in value:
            ret['name'] = re.sub('Name: ', '', value)
        elif 'Group' in value:
            ret['group'] = re.sub('Group: ', '', value)
        elif 'Result' in value:
            ret['result'] = re.sub('Result: ', '', value)
        elif 'Percentile' in value:
            if 'Theory Percentile' in value:
                theory_percentile = re.sub('Theory Percentile: ', '', value)
                ret['th_p'] = re.sub('\n', '', theory_percentile)
            elif 'Science Percentile' in value:
                ret['sci_p'] = re.sub('Science Percentile: ', '', value)
            else:
                ret['percentile'] = re.sub('Percentile: ', '', value)
    # print('Seat No:'+seat_no)
    # print('Name;'+ name)
    # print('Group:'+group)
    # print('Result:'+result)
    # print('Theory Percentile:'+theory_percentile)
    # print('Science Percentile:'+science_percentile)
    # print('Percentile:'+percentile)

    for i in range(len(subject)):
        if '013' in subject[i]:
            ret['eng_sl'] = marks[i]
        elif '050' in subject[i]:
            ret['maths'] = marks[i]
        elif '052' in subject[i]:
            ret['chem'] = marks[i]
        elif '053' in subject[i]:
            ret['chem_prac'] = marks[i]
        elif '054' in subject[i]:
            ret['phy'] = marks[i]
        elif '055' in subject[i]:
            ret['phy_prac'] = marks[i]
        elif '056' in subject[i]:
            ret['bio'] = marks[i]
        elif '057' in subject[i]:
            ret['bio_prac'] = marks[i]
        elif '331' in subject[i]:
            ret['com'] = marks[i]
        elif '332' in subject[i]:
            ret['com_prac'] = marks[i]
        elif '129' in subject[i]:
            ret['sanskrit'] = marks[i]
        elif 'Total' in subject[i]:
            ret['total'] = marks[i]
            ret['grade'] = grade[i]
    return ret

def analyse_10(content):
    soup = BeautifulSoup(content, 'html.parser')
    subject = []
    marks = []
    grade = []
    temp = []
    ret = {}
    for tr in soup.find_all('tr'):
        spans = tr.find_all('span')
        if (len(spans) == 0):
            tds = tr.find_all('td')
            
            if len(tds) == 5 and tds[0].get_text() != 'Subject Name':
                if tds[0].get_text().startswith('01'):
                    ret['guj_board'] = tds[1].get_text()
                    ret['guj_school'] = tds[2].get_text()
                    ret['guj_total'] = tds[3].get_text()
                    ret['guj_grade'] = tds[4].get_text()
                elif tds[0].get_text().startswith('10'):
                    ret['ss_board'] = tds[1].get_text()
                    ret['ss_school'] = tds[2].get_text()
                    ret['ss_total'] = tds[3].get_text()
                    ret['ss_grade'] = tds[4].get_text()
                elif tds[0].get_text().startswith('11'):
                    ret['sci_board'] = tds[1].get_text()
                    ret['sci_school'] = tds[2].get_text()
                    ret['sci_total'] = tds[3].get_text()
                    ret['sci_grade'] = tds[4].get_text()
                elif tds[0].get_text().startswith('17'):
                    ret['san_board'] = tds[1].get_text()
                    ret['san_school'] = tds[2].get_text()
                    ret['san_total'] = tds[3].get_text()
                    ret['san_grade'] = tds[4].get_text()
                elif tds[0].get_text().startswith('16'):
                    ret['eng_board'] = tds[1].get_text()
                    ret['eng_school'] = tds[2].get_text()
                    ret['eng_total'] = tds[3].get_text()
                    ret['eng_grade'] = tds[4].get_text()
                elif tds[0].get_text().startswith('12'):
                    ret['math_board'] = tds[1].get_text()
                    ret['math_school'] = tds[2].get_text()
                    ret['math_total'] = tds[3].get_text()
                    ret['math_grade'] = tds[4].get_text()
                else:
                    print(f'new subject {tds[0].get_text()}')

            elif len(tds) == 4:
                pass

            elif len(tds) == 3:
                pass


            elif len(tds) == 2:
                if tds[0].get_text() == 'Grand Total':
                    ret['total'] = tds[1].get_text().split('(')[0][:-1] 
                elif tds[0].get_text() == '24 COMPUTER EDU.-T':
                    ret['com_theo'] = tds[1].get_text()
                elif tds[0].get_text() == '51 COMPUTER EDU.-P':
                    ret['com_prac'] = tds[1].get_text()
                elif tds[0].get_text() in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D', 'E']:
                    ret['grade'] = tds[0].get_text()
                    ret['percentile'] = tds[1].get_text()
                

        elif (len(spans) == 1):
            temp.append(spans[0].get_text())
        elif (len(spans) == 2):
            temp.append(spans[0].get_text())
            temp.append(spans[1].get_text())
        else:
            subject.append(spans[0].get_text())
            marks.append(spans[2].get_text())
            grade.append(spans[3].get_text())

    for value in temp:
        if 'Seat No' in value:
            ret['seat'] = re.sub('Seat No: ', '', value)
        elif 'Name' in value:
            ret['name'] = re.sub('Name: ', '', value)
        elif 'Result' in value:
            ret['result'] = re.sub('Result: ', '', value)

    return ret