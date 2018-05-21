import os
rollnumber = 'B356897'

def make_html(rollnumber):
    first = rollnumber[0]+rollnumber[1]+rollnumber[2]
    second = rollnumber[3]+rollnumber[4]
    if(os.system('wget http://gseb.org/522lacigam/sci/'+first+'/'+second+'/'+rollnumber+'.html')):
        os.system('mv '+rollnumber+'.html ~/Project/Result')
        return True
    else:
        return False

make_html(rollnumber)