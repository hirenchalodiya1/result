from bs4 import BeautifulSoup

rollnumber = 'B123789'


def analyse(rollnumber):
    with open(rollnumber + '.html', 'r') as content_file:
        file = content_file.read()
    soup = BeautifulSoup(file, 'html.parser')
    for tr in soup.find_all('tr'):
        spans = tr.find_all('span')
        if(len(spans)<3):
            None
        else:
            print(spans[0].get_text())

        # for span in tr.find_all('span'):
        #     spantext = span.get_text()
        #     print(spantext)
        # if spantext[0] is '013 ENGLISH (S.L.)':
        #     print('English marks is'+spantext[0])


analyse(rollnumber)
