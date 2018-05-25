from bs4 import BeautifulSoup
import re
from takehtml import make_html

def analyse_12science(rollnumber):
    try:
        with open(rollnumber + '.html', 'r') as content_file:
            file = content_file.read()
        content_file.close()
        soup = BeautifulSoup(file, 'html.parser')
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

        for value in temp:
            if 'Seat No' in value:            seat_no = re.sub('Seat No: ', '', value)
            elif 'Name' in value:            name = re.sub('Name: ', '', value)
            elif 'Group' in value:            group = re.sub('Group: ', '', value)
            elif 'Result' in value:            result = re.sub('Result: ', '', value)
            elif 'Percentile' in value:
                if 'Theory Percentile' in value:
                    theory_percentile = re.sub('Theory Percentile: ', '', value)
                    theory_percentile = re.sub('\n', '', theory_percentile)
                elif 'Science Percentile' in value:
                    science_percentile = re.sub('Science Percentile: ', '', value)
                else:
                    percentile = re.sub('Percentile: ', '', value)
        # print('Seat No:'+seat_no)
        # print('Name;'+ name)
        # print('Group:'+group)
        # print('Result:'+result)
        # print('Theory Percentile:'+theory_percentile)
        # print('Science Percentile:'+science_percentile)
        # print('Percentile:'+percentile)

        for i in range(len(subject)):
            if '013' in subject[i]:             english_sl = marks[i]
            elif '050' in subject[i]:            mathematics = marks[i]
            elif '052' in subject[i]:            chemistry = marks[i]
            elif '053' in subject[i]:            chemistry_prac = marks[i]
            elif '054' in subject[i]:            physics = marks[i]
            elif '055' in subject[i]:            physics_prac = marks[i]
            elif '056' in subject[i]:            biology = marks[i]
            elif '057' in subject[i]:            biology_prac = marks[i]
            elif '331' in subject[i]:            computer = marks[i]
            elif '332' in subject[i]:            computer_prac = marks[i]
            elif '129' in subject[i]:            sanskrit = marks[i]
            elif 'Total' in subject[i]:
                total = marks[i]
                overall_grade = grade[i]
        if 'A' in group:
            return (seat_no, name, group, result, percentile, science_percentile, theory_percentile, english_sl, mathematics, chemistry, chemistry_prac, physics, physics_prac, computer, computer_prac, total, overall_grade)
        else:
            return (seat_no,name,group,result,percentile,science_percentile,theory_percentile,english_sl,biology_prac,biology,chemistry,chemistry_prac,physics,physics_prac,computer,computer_prac,total,overall_grade)
    except:
        make_html(rollnumber)
        analyse_12science(rollnumber)