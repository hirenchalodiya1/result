from bs4 import BeautifulSoup
import os

def analyse(rollnumber):
    with open(rollnumber + '.html', 'r') as content_file:
        file = content_file.read()
    content_file.close()
    soup = BeautifulSoup(file, 'html.parser')
    marks = []
    for tr in soup.find_all('tr')[5:]:
        spans = tr.find_all('span')
        if(len(spans)<3):
            pass
        else:
            marks.append(spans[2].get_text())
    os.system('rm '+rollnumber+'.html')
    return marks